import datetime
import random
from enum import Enum

import cv2
import numpy
import win32con
import win32gui
import win32print
from PIL import Image

from _PartLogger import *

pystart = datetime.datetime.now()

dvWidth = win32print.GetDeviceCaps(win32gui.GetDC(0), win32con.DESKTOPHORZRES)
dvHeight = win32print.GetDeviceCaps(win32gui.GetDC(0), win32con.DESKTOPVERTRES)

uiWidth = win32gui.GetWindowRect(win32gui.GetDesktopWindow())[2]
uiHeight = win32gui.GetWindowRect(win32gui.GetDesktopWindow())[3]

uiScale = dvWidth / uiWidth

muTitle = 32 - 2

muWidth = int(1280 / uiScale)
muHeight = int(720 / uiScale) + muTitle

cvWidth = int(1280)
cvHeight = int(720)

vmWidth = int(1920)
vmHeight = int(1080)

cvScale = vmHeight / cvHeight

roiFull = (0, 0, 1280, 720)
fbNone = (-2, -2, -2, -2)
fbSelf = (-1, -1, -1, -1)

retNone = False
retTimeout = False
retFind = True
retHoldFail = False
xyFalse = (False, False)

def GetFBXY(xy, tl=None) :
    if len(xy) == 2 :  # 长度2 > 结果坐标 > 计算随机
        if tl is None :
            logger.error('GetFBXY: 没有范围输入，无法计算区域随机数!')
            return 0, 0
        if type(tl).__name__ == typeTL :
            if len(tl.FB) == 5 :  # 模板类范围 > 有xy偏移标志 > 相对范围
                xy = xy[0] + tl.FB[0], xy[1] + tl.FB[1]
                return (random.randint(xy[0], xy[0] + tl.FB[2]),
                        random.randint(xy[1], xy[1] + tl.FB[3]))
            if len(tl.FB) == 4 :  # 模板类范围 > 只有两组坐标 > 绝对范围
                return (random.randint(tl.FB[0], tl.FB[2]),
                        random.randint(tl.FB[1], tl.FB[3]))
        if len(tl) == 4 :  # 自定义范围 > 自定义相对范围
            return (random.randint(int(xy[0] + tl[0]), int(xy[0] + tl[2])),
                    random.randint(int(xy[1] + tl[1]), int(xy[1] + tl[3])))
        pass  # if typeTL

    if len(xy) == 4 :  # 长度4 > 自定义范围 > 直接计算随机
        return (random.randint(int(xy[0]), int(xy[2])),
                random.randint(int(xy[1]), int(xy[3])))

    print(xy, len(xy))
    logger.error('GetFBXY: 无效范围输入，无法计算区域随机数!')
    logger.error('         ?? %s' % type(xy))
    return 0, 0

class mo(Enum) :
    SELF = -1
    TL = LT = 1
    TC = CT = 2
    TR = RT = 3
    CL = LC = 4
    CC = 5
    CR = RC = 6
    BL = LB = 7
    BC = CB = 8
    BR = RB = 9

def cal(pos0, mv1, mv2, mv3, mv4) :
    """
    原点设为 图像 底部中心 Center + Bottom 计算区域
    若 pos0 输入 mo.SELF 则以如下区间计算随机坐标
    (结果偏移 mv1,mv2 为起点选定 mv3,mv4 大小区域)

    :param pos0: 原点位置 Enum pos.*
    :param mv1: 区域 左上角 偏移量
    :param mv2: 区域 右上角 偏移量
    :param mv3: 区域 左下角 偏移量
    :param mv4: 区域 右下角 偏移量
    :return: 偏移后的区域 (x1,y1,x2,y2)

    LT　　　　　　 　 CT　　　　　　　RT
    　　┌　　　　　　┬　　　　　　┐　

    LC　├　　　　 　 CC　　　 　 　┤　RC

    　　└　　　　　　┴　　　　　　┘　
    LB　　　　　　 　 CB　　　　　　　RB
    　
    """

    if pos0 == mo.SELF :
        logger.info('   CAL < ↖(%s,%s) ↘(%s,%s) %s > Self ' % (mv1, mv2, mv3, mv4, pos0))
        return (int(mv1 * cvScale), int(mv2 * cvScale),
                int(mv3 * cvScale), int(mv3 * cvScale),
                pos0)

    elif pos0 == mo.LT : origin = (1, 1)
    elif pos0 == mo.CT : origin = (cvWidth / 2, 1)
    elif pos0 == mo.RT : origin = (cvWidth, 1)
    elif pos0 == mo.LC : origin = (1, cvHeight / 2)
    elif pos0 == mo.CC : origin = (cvWidth / 2, cvHeight / 2)
    elif pos0 == mo.RC : origin = (cvWidth, cvHeight / 2)
    elif pos0 == mo.LB : origin = (1, cvHeight)
    elif pos0 == mo.CB : origin = (cvWidth / 2, cvHeight)
    elif pos0 == mo.RB : origin = (cvWidth, cvHeight)
    else : origin = (1, 1)

    mv1 = int(origin[0] - 1 + mv1)
    mv2 = int(origin[1] - 1 + mv2)
    mv3 = int(origin[0] - 1 + mv3)
    mv4 = int(origin[1] - 1 + mv4)
    logger.info('   CAL < ↘(%s,%s) ↘(%s,%s) > Screen ' % (mv1, mv2, mv3, mv4))
    return (int(mv1 * cvScale), int(mv2 * cvScale),
            int(mv3 * cvScale), int(mv3 * cvScale))

class definetl :
    Gray = 1
    RGB = 3
    RGBA = 4

    def __init__(self, root, path, text, ROI=roiFull, FB=fbSelf, param=None) :
        """
        定义模板对象，内部包含：注释、图像矩阵、感兴趣区域、反馈区域

        关于透明模板：透明匹配为提高识别率
        　　  　　　 　 将强制使用RGB分离匹配坐标判断，
        　　  　　　 　 准备灰度透明模板没意义，
        　　  　　　 　 对CV而言且还是以RGBA格式导入

        提示：并不是 没有透明区域的图像就没有透明度通道，
        　　 　例如PS中没有进行合并图像操作就保存的PNG文件

        探索：Windows资源管理器右键一个灰度8bit透明PNG文件的属性
        　　 　详细信息内的位深度显示为 32 也就是 8+8+8+8 四通道
        　　 　而无透明度通道的灰度8bit的PNG文件的位深度会显示 8

        :param root: 资源根目录，格式 "//root//"
        :param path: 模板图像相对根路径，格式 "filename.png"
        :param text: 日志输出的注释信息，字符串
        :param ROI: 感兴趣区域，格式 (x1,y2,x2,y2)
        :param FB: 输入反馈区域，格式 (x1,y2,x2,y2)
        :param param: 额外参数，可选[ForceGray]
        """

        if type(param).__name__ != 'list' : param = [param]

        if root is None : pass  # GetTypeUse
        else :
            self.text = text
            self.ROI = ROI
            self.FB = FB

            self.space = None
            self.alpha = None
            self.channel = None

            if self.RGB in param : imflags = cv2.IMREAD_COLOR

            elif self.RGBA in param : imflags = cv2.IMREAD_UNCHANGED

            elif self.Gray in param : imflags = cv2.IMREAD_GRAYSCALE

            else : imflags = cv2.IMREAD_COLOR

            # 读取原始图像内容
            ASCII = False
            path = root + path

            if ASCII :
                self.array = cv2.imread(path, flags=imflags)

                if len(self.array.shape) == 3 : self.channel = self.array.shape[2]
                elif len(self.array.shape) == 2 : self.channel = 1

                if self.channel == 1 :
                    self.space = self.Gray
                elif self.channel == 3 :
                    self.space = self.RGB
                elif self.channel == 4 :
                    self.space = self.RGBA
                    self.alpha = cv2.split(self.array)[3]
                    self.array = cv2.cvtColor(self.array, cv2.COLOR_BGRA2BGR)

            else :
                pilHandle = Image.open(path)
                pilCh = pilHandle.split()
                if len(pilCh) == 4 and imflags == cv2.IMREAD_UNCHANGED :
                    if numpy.sum(numpy.asarray(pilCh[3]) == 255) == \
                            int(pilHandle.size[0] * pilHandle.size[1]) :
                        logger.warning(' ↓↓↓ 无效的全白Alpha通道[%s]' % path)
                        self.space = self.RGB
                        self.array = cv2.merge([numpy.asarray(pilCh[2]),
                                                numpy.asarray(pilCh[1]),
                                                numpy.asarray(pilCh[0])])
                        self.channel = 3
                    else :
                        self.space = self.RGBA
                        self.array = cv2.merge([numpy.asarray(pilCh[2]),
                                                numpy.asarray(pilCh[1]),
                                                numpy.asarray(pilCh[0]),
                                                numpy.asarray(pilCh[3])])
                        self.alpha = numpy.asarray(pilCh[3])
                        self.channel = 4
                elif len(pilCh) == 1 and imflags == cv2.IMREAD_GRAYSCALE :
                    self.space = self.Gray
                    self.array = numpy.asarray(pilHandle)
                    self.channel = 1
                else :
                    if len(pilCh) == 1 : pilCh = [pilCh[0], pilCh[0], pilCh[0]]

                    self.space = self.RGB
                    self.array = cv2.merge([numpy.asarray(pilCh[2]),
                                            numpy.asarray(pilCh[1]),
                                            numpy.asarray(pilCh[0])])
                    self.channel = 3

            # 获取图像结构信息
            self.width = self.array.shape[1]
            self.height = self.array.shape[0]

            logger.info("定义特征[%s] {%s} {%dw%dh %dc}" % (self.text, path.replace('.\\', ''), self.width, self.height, self.channel))
            logger.debug('-----------------------------------------------------------------------')
        pass  # getType

    # def __call__(self) : return self.array

typeTL = type(definetl(None, None, None, None)).__name__

if __name__ == '__main__' :
    # print(GetInt((100, 100), res=(20, 20, 20, 20)))
    # Next = definetl(definetl.RGB, ".\\PCR1280x720\\", "#00-0.png", "测试:AAAA")
    # print(type(Next).__name__ == typeTL)
    # print(cal(mo.CB, -610, -60, -442, 0))
    b = definetl(".\\PCR1280x720\\", "#43_0_1.png", "冒险:极难3", roiFull, fbSelf, [definetl.RGB])
    d = definetl(".\\PCR1280x720\\", "#43-0-1F.png", "地下城:1F", roiFull, fbSelf, [definetl.RGBA])

    cv2.imshow('aaa', b.array)
    cv2.waitKey(1000 * 2)
    cv2.imshow('aaa', d.array)
    cv2.waitKey(1000 * 2)
    cv2.imshow('aaa', d.alpha)
    cv2.waitKey(1000 * 2)
