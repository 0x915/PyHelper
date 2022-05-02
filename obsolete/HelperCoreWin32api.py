from _public import *

import win32ui
import win32gui
import win32con
import win32print

from win32api import GetSystemMetrics

def GetDPIPercent():
    PhyW = win32print.GetDeviceCaps(win32gui.GetDC(0), win32con.DESKTOPHORZRES)
    PhyH = win32print.GetDeviceCaps(win32gui.GetDC(0), win32con.DESKTOPVERTRES)
    SysW = GetSystemMetrics(0)
    SysH = GetSystemMetrics(1)
    return PhyW/SysW
FIX=GetDPIPercent()

window=[];
def GetWINhandler(hwnd,Inlist=window):
    Inlist.append({
        'handle' : hwnd, 
        'class'  : win32gui.GetClassName(hwnd),
        'title'  : win32gui.GetWindowText(hwnd),
        'pos'    : win32gui.GetWindowRect(hwnd)
        })

target=[];
def GetVMhandler() :
    global window,target;window=[];target=[];num=0;
    win32gui.EnumWindows(GetWINhandler,window)
    for i in window :
        if i['class']=='Qt5QWindowIcon' and i['title']!='MEmu' and i['title']!='逍遥多开器': 
            GetWINhandler(i['handle'],target);
            ID = (str(i['title']).replace("(","")).replace(")","")
            print('Handler'+str(num),'搜索到模拟器窗口'+str(i['title'])+'['+str(i['handle'])+']'+str(i['pos'])+'')
            check=numpy.array(win32gui.GetWindowRect(win32gui.GetDesktopWindow()))>numpy.array(i['pos'])
            if win32gui.IsIconic(i['handle']) : 
                print(ID,'窗口取消最小化，为保证脚本正常运行，请勿最小化，可使用Win10多桌面放置窗口');
                win32gui.ShowWindow(i['handle'],win32con.SW_RESTORE);
            elif (check==numpy.array([False,False,True,True])).all() : 
                print(ID,'窗口状态正常，为保证脚本正常运行，请勿最小化，可使用Win10多桌面放置窗口');
            else : print(ID,'窗口超出本屏幕范围，单显示器可能会影响监视，多显示器可以无视');
            num = num + 1;
    if len(target)==0 : print('Handler','未检测到MEMU安卓虚拟机窗口');exit();

i=0;
def GetScreen32GUI(ID=0,debug=0) :
    global i;
    start = datetime.datetime.now();
    hWnd = target[ID]['handle']
    while(i) :
        if ID==0 : win32gui.SetWindowPos(hWnd,win32con.HWND_BOTTOM,0,0,SetW+2,SetH+34,win32con.SWP_DRAWFRAME)
        if ID==1 : win32gui.SetWindowPos(hWnd,win32con.HWND_BOTTOM,SetW,0,SetW+2,SetH+34,win32con.SWP_DRAWFRAME)
        i=0;
    hWnd = win32gui.FindWindowEx(hWnd,0,'Qt5QWindowIcon','MainWindowWindow');
    hWnd = win32gui.FindWindowEx(hWnd,0,'Qt5QWindowIcon','CenterWidgetWindow');
    hWnd = win32gui.FindWindowEx(hWnd,0,'Qt5QWindowIcon','RenderWindowWindow');

    L, T, R, B = win32gui.GetWindowRect(hWnd)
    width = int((R - L)*FIX); height = int((B - T)*FIX);
    hWndDC = win32gui.GetWindowDC(hWnd)#创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)#创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()#创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()#为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)#将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)#保存bitmap到内存设备描述表
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)
    signedIntsArray = saveBitMap.GetBitmapBits(True)

    im_opencv = numpy.frombuffer(signedIntsArray, dtype = 'uint8')
    im_opencv.shape = (height, width, 4)
    im_opencv = cv2.resize(im_opencv,(SetW,SetH), interpolation=cv2.INTER_NEAREST);
    if 0 :
        cv2.imshow("im_opencv",im_opencv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd,hWndDC)

    end = datetime.datetime.now();
    if debug : print(str(end-start)[2:11],'获取WinGUI窗口 '+target[ID]['title']+' 画面');
    return im_opencv

VM = GetScreen32GUI()
cv2.imwrite('1.png', VM)