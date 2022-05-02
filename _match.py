import datetime
from enum import Enum

import cv2
import numpy

from _public import cvScale, typeTL, xyFalse
from _logger import logger

def crop(mat, tlclass) : return mat[tlclass.ROI[1] :tlclass.ROI[3], tlclass.ROI[0] :tlclass.ROI[2]]

class mt(Enum) :
    SELF = -1
    null = 0
    gray = 1
    rgb = 3
    rate = 4
    exact = 5
    quiet = 6
    debug = 7
    multi = 9
    count = 10
    raw = 99
    mixed = 100

def matchtl(screen, tlclass, threshold=0.8, param=None) :
    """
        自动类型匹配 -- 按照 tlclass.alpha 属性分配 识别方式
        param 独有 mt.count 可配置为计数模式(仅限无mask匹配)

        :param screen    > 背景输入，接受 numpy arrag() 对象
        :param tlclass   > 模板类输入，接受 class definetl() 对象
        :param threshold > 匹配阈值，接受 float 类型
        :param param     > 控制参数，参考后级函数
        :return 匹配成功返回(X,Y) 失败返回(False,False) 计数返回[count,(x1,y1),...]
    """

    if type(tlclass).__name__ != 'list' : tlclass = [tlclass]
    if type(param).__name__ != 'list' : param = [param]
    count = True if mt.count in param else False

    for tl in tlclass :
        if type(tl).__name__ != typeTL :
            logger.error('match.rect 模板类型异常 %s ≠ input(%s)' % (typeTL, type(tl)))
            exit()

        if tl.alpha is None :
            if count :
                count_t = [0]
                matlist = rect(screen, tl, threshold, param)
                if matlist == xyFalse : return xyFalse
                for mat in matlist :
                    while True :
                        count_old = count_t[0]
                        min_val, val, min_loc, loc = cv2.minMaxLoc(mat)
                        if val > threshold :
                            count_t.append([int(loc[0] * cvScale), int(loc[1] * cvScale)])
                            count_t[0] += 1
                            mat[loc[1]][loc[0]] = 0
                            rectpt1 = loc[0] - int(tl.width / 2), loc[1] - int(tl.height / 2)
                            rectpt2 = loc[0] + int(tl.width / 2), loc[1] + int(tl.height / 2)
                            mat = cv2.rectangle(mat,rectpt1,rectpt2,(0,0,0),-1)
                        if count_old == count_t[0] : break
                    pass  # while count
                    return count_t if count_t[0] != 0 else None
                pass  # for matlist
            pass  # if count
            xy = rect(screen, tl, threshold, param)
            if xy != xyFalse : return xy
        else :
            xy = mask(screen, tl, threshold, param)
            if xy != xyFalse : return xy

    return xyFalse

def mask(screen, tlclass, threshold=0.8, param=None) :
    """
        蒙版区域匹配 -- 输入 MaskMat 的影响对应像素结果的权重

        :param screen    > 背景输入，接受 numpy arrag() 对象
        :param tlclass   > 模板类输入，接受 class definetl() 对象
        :param threshold > 匹配阈值，接受 float 类型
        :param param     > 控制参数，接受 Enum mt.* quiet静默执行、mixed混合结果
        :return 匹配成功返回(X,Y) 失败返回(False,False)
    """

    if type(param).__name__ != 'list' : param = [param]
    quiet = True if mt.quiet in param else False
    debug = True if mt.debug in param else False
    mixed = True if mt.mixed in param else False

    raw = True if (mt.raw in param) or (mt.count in param) else False
    start = datetime.datetime.now()

    templ = tlclass.array
    alpha = tlclass.alpha

    sum_t = [0, 0]
    rate_t = list()
    match_t = list()
    result_t = list()

    # 三通道坐标匹配
    for (vm, templ) in zip(cv2.split(screen), cv2.split(templ)) :
        match = cv2.matchTemplate(vm, templ, method=cv2.TM_CCORR_NORMED, mask=alpha)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)
        rate_t.append(max_val)
        result_t.append(numpy.array(max_loc))
        match_t.append(match)

    if debug :
        print(tlclass.text)
        logger.debug('\n\nMATCH MASK\n    | %s\n    | %s' % (result_t, rate_t))

    if mixed :
        # 平均权重混合判定
        match_t = [match_t[0] / 3 + match_t[1] / 3 + match_t[2] / 3]
        min_val, rate, min_loc, result = cv2.minMaxLoc(match_t[0])

    else :
        # 点集欧式距离判定
        for i in range(-1, len(result_t) - 1) :
            if numpy.linalg.norm(result_t[i] - result_t[i + 1]) > 20 :
                return xyFalse
        rate = min(rate_t)
        for result in result_t :
            sum_t = sum_t[0] + result[0], sum_t[1] + result[1]
        result = (int(sum_t[0] / len(result_t)), int(sum_t[1] / len(result_t)))

    if threshold < 0.95 : threshold = 0.95
    if rate < threshold : return xyFalse

    end = datetime.datetime.now()
    if raw : return match_t

    if debug : drawResult(screen, result)

    # w/2 h/2 < 纠正结果 为 模板中心 >
    # scaling < VM 渲染窗口 和 实际分辨率 的倍数差 >
    result = (result[0] + int(tlclass.width / 2), result[1] + int(tlclass.height / 2))
    result = (int(result[0] * cvScale), int(result[1] * cvScale))

    if not quiet :
        extstring = "Extra:" + 'MIXED' if mixed else ''
        logger.info('MATCH MASK(%s)=%s %s%% %sms %s' % (
            tlclass.text, str(result).replace(' ', ''),
            str(int(rate * 100)),
            str((end - start).microseconds)[:-3],
            extstring))

    return result

def rect(screen, tlclass, threshold=0.8, param=None) :
    """
        矩形区域匹配 -- 输入 TemplMat 的所有像素将会影响 匹配结果

        :param screen    > 背景输入，接受 numpy arrag() 对象
        :param tlclass   > 模板类输入，接受 class definetl() 对象
        :param threshold > 匹配阈值，接受 float 类型
        :param param     > 控制参数，接受 Enum mt.* rgb彩色识别、quiet静默执行
        :return 匹配成功返回(X,Y) 失败返回(False,False)
    """

    if type(param).__name__ != 'list' : param = [param]
    color = True if mt.rgb in param else False
    quiet = True if mt.quiet in param else False
    debug = True if mt.debug in param else False

    raw = True if (mt.raw in param) or (mt.count in param) else False
    start = datetime.datetime.now()

    templ = tlclass.array

    # space < cv2.matchTemplate(image,templ) 必须输入匹配的 mat >
    #       < 灰度图 shape 只有两个长度 height width            >
    #       < 彩色图 shape 有三个长度 height width channel      >
    if not color :
        if len(templ.shape) != 2 : templ = cv2.cvtColor(templ, cv2.COLOR_BGR2GRAY)
        if len(screen.shape) != 2 : screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    else :
        if len(templ.shape) == 2 : templ = cv2.cvtColor(templ, cv2.COLOR_GRAY2BGR)
        if len(screen.shape) == 2 : screen = cv2.cvtColor(screen, cv2.COLOR_GRAY2BGR)

    match = cv2.matchTemplate(image=screen, templ=templ, method=cv2.TM_CCOEFF_NORMED)

    # SQDIFF < 差值平方和匹配 返回矩阵 float 暗点 高匹配率 >
    # rate, max_val, result, max_loc = cv2.minMaxLoc(match)
    # CCOEFF <      相关匹配 返回矩阵 float 亮点 高匹配率 >
    min_loc, rate, min_loc, result = cv2.minMaxLoc(match)

    if mt.rate in param : return rate
    if rate < threshold : return xyFalse

    end = datetime.datetime.now()
    if raw : return [match]

    if debug : drawResult(screen, result)

    # w/2 h/2 < 纠正结果 为 模板中心 >
    # scaling < VM 渲染窗口 和 实际分辨率 的倍数差 >
    result = (result[0] + int(tlclass.width / 2), result[1] + int(tlclass.height / 2))
    result = (int(result[0] * cvScale), int(result[1] * cvScale))

    if not quiet :
        logger.info('MATCH RECT(%s)=%s %s%% %sms' % (
            tlclass.text, str(result).replace(' ', ''),
            str(int(rate * 100)),
            str((end - start).microseconds)[:-3]))

    return result

def drawResult(screen, result) :
    if type(result).__name__ != 'list' : result = [result]
    if len(screen.shape) != 2 : screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    for xy in result :
        screen = cv2.circle(cv2.cvtColor(screen, cv2.COLOR_GRAY2BGR), xy, 4, (0, 255, 0), 8)
    cv2.imshow("DebugMATCH", screen)
    cv2.waitKey(1000 * 2)

if __name__ == '__main__' :
    from pcr_tl import PCR
    from _platform import GetMuHandler
    from _android import mudevice

    MEMU = mudevice("127.0.0.1:21503", "(VM)", "/dev/input/event6")
    MEMU.connect()

    GetMuHandler()
    # os.system('cls')
    print('')
    # Next = DefTarget(".\\PCR1280x720\\AT01Next.png", "推图:下一步", (0, 0, 1280, 720), NoneOrSelf)
    image = cv2.imread('.\\debug\\220412.010259.bmp')

    while True :
        matchtl(MEMU.GetScreen(), PCR['商店:通常售完'], 0.9, [])
        print(matchtl(MEMU.GetScreen(), PCR['商店:通常售完'], 0.9, [mt.count]))
        exit()
        # matchtl(MEMU.GetScreen(), lnext[0], 0.975, [mt.rate])
        # if xy!=xyFalse :
        #     if anext is None :
        #         t = MEMU.GetScreen()
        #
        #     touch = GetFBXY(xy, lnext)
        #     MEMU.inputTouch(touch)
        #     time.sleep(1000)

        # rect(image, PCR['导航:冒险'][0], 0.9, [mt.gray])
        # mask(MEMU.GetScreen(), PCR['战斗:下一关'], 0.9, [])
        # MATCH_MULTI(GetVMScreen(), PCR.Res10_5, 0.98, debug=True)
        # print(MATCH_COUNT(GetVMScreen(), PCR.Res99_2_3))
    pass
