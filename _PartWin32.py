import time

import numpy
import win32ui

from _PartEnv import *

window = list()
target = dict()

def GetWinHandler(hWnd, Inlist) :
    Inlist.append({
        'handle' : hWnd,
        'class'  : win32gui.GetClassName(hWnd),
        'title'  : win32gui.GetWindowText(hWnd),
        'pos'    : win32gui.GetWindowRect(hWnd)
    })

MuList = [
    # 黑名单 相等
    ['NemuService', 'NemuPlayer', ],
    # 黑名单 包含
    ['MEmu', '逍遥多开'],
    # 白名单 相等
    ['Qt5QWindowIcon', ],
    # 白名单 包含
    [],
]

def HandleBlack(string) :
    for i in MuList[0] :
        if string == i : return False
    for i in MuList[1] :
        if i in string : return False
    return True

def HandleWhile(string) :
    for i in MuList[2] :
        if string == i : return True
    for i in MuList[3] :
        if i in string : return True
    return False

def GetMuHandler() :
    global window, target
    window = list()
    target = dict()
    count = 0
    win32gui.EnumWindows(GetWinHandler, window)
    logger.info('更新Mu主窗句柄 SYS(%dx%d < %s < %dx%d) \n' % (uiWidth, uiHeight, str(int(uiScale * 100)) + '%', dvWidth, dvHeight))

    for i in window :
        if HandleWhile(i['class']) and HandleBlack(i['title']) :
            count, hWnd, title, pos = count + 1, i['handle'], i['title'], i['pos']
            logger.info('Mu主窗 标题[%s] Handle(%s) Pos%s ' % (title, hWnd, pos))
            while win32gui.IsIconic(hWnd) :
                # win32gui.ShowWindow(hWnd,win32con.SW_SHOWNA);
                logger.warning('等待窗口 ... 脚本正常 ? 时 勿最小化，可使用 ? 面放 ?窗口')
                while win32gui.IsIconic(i['handle']) : pass
            # target.append({'handle' : hWnd, 'title' : title, 'pos' : pos})
            target[i['title']] = {'handle' : hWnd, 'title' : title, 'pos' : pos}
            target[str(count)] = {'handle' : hWnd, 'title' : title, 'pos' : pos}

    if len(target) == 0 :
        logger.error('未检测到VM画面窗口')
        exit()

def GetVMScreen(title=None, handle=None, num=0, Mu='MEMU',quiet=True) :
    start  = datetime.datetime.now()
    if title is None and type(num).__name__ != 'int' and handle is None :
        logger.error('没有指定MU窗口 标题 "%s" num[%s] handle[%s]' % (title, num, handle))
        exit()

    if title is not None and handle is None :
        if title in target.keys() :
            handle = target[title]['handle']
        else :
            logger.error('列表内不存在该标题的MU窗口 标题 "%s" 重新获取列表...' % title)
            GetMuHandler()
            if title in target.keys() : handle = target[title]['handle']
            else :
                logger.error('重新获取列表后依然不存在 标题 "%s"' % title)
                exit()

    elif handle is not None and title is None :
        handle = handle

    else :
        logger.error('只能指定一个搜索项 标题 "%s" handle[%s]' % (title, handle))
        handle = None
        exit()

    pos = win32gui.GetWindowRect(handle)
    win32gui.SetWindowPos(handle, None, pos[0], pos[1], muWidth, muHeight, win32con.SWP_NOMOVE)  # , win32con.SWP_SHOWWINDOW

    if Mu == 'MUMU' :
        hWnd = win32gui.FindWindowEx(handle, 0, 'Qt5QWindowIcon', None)
        hWnd = win32gui.FindWindowEx(hWnd, 0, 'canvasWin', None)
    elif Mu == 'MEMU' :
        hWnd = win32gui.FindWindowEx(handle, 0, 'Qt5QWindowIcon', 'MainWindowWindow')
        hWnd = win32gui.FindWindowEx(hWnd, 0, 'Qt5QWindowIcon', 'CenterWidgetWindow')
        hWnd = win32gui.FindWindowEx(hWnd, 0, 'Qt5QWindowIcon', 'RenderWindowWindow')
    else :
        hWnd = None
        logger.error('没有适配的MU平台 Mu[%s] handle[%s]' % (Mu, hWnd))
        exit()


    hWndDC = win32gui.GetWindowDC(hWnd)
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, cvWidth, cvHeight)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (cvWidth, cvHeight), mfcDC, (0, 0), win32con.SRCCOPY)
    signedIntsArray = saveBitMap.GetBitmapBits(True)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd, hWndDC)

    im = numpy.frombuffer(signedIntsArray, dtype='uint8')
    im.shape = (cvHeight, cvWidth, 4)
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # if UIScale==2 : im = cv2.resize(im,(0, 0),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
    end = datetime.datetime.now()
    if not quiet :logger.info('获取窗口画面(%dx%d)耗时 %s ms'%(cvWidth,cvHeight,str((end-start).microseconds)[:-3]))
    return cv2.cvtColor(im, cv2.COLOR_BGRA2BGR)

if __name__ == '__main__' :
    GetMuHandler()
    while True :
        VM = GetVMScreen(title='VM')
        # VM = cv2.resize(VM,(960, 540), interpolation=cv2.INTER_AREA)
        save = 'debug\\' + time.strftime('%Y%m%d.%H%M%S', time.localtime(time.time()))[2 :] + '.tif'
        cv2.imwrite(save, VM)
        logger.info('保存截图 ' + save)
        exit()
