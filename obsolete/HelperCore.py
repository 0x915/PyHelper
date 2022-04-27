
import cv2
import os
import sys
import time
import numpy
import random
import win32ui
import win32gui
import win32con
import datetime
import colorama
import keyboard
import subprocess
import urllib.request as urllib
from colorama import init,Fore,Back,Style

init(autoreset=True)

memu1adb = '127.0.0.1:21513'
memu1trm = '127.0.0.1:18080'

os.system("cls")

def ADBConnect(IP) :
    if ':' in IP and '.' in IP :
        subprocess.call("adb connect "+IP,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ptinfo('ADB','连接调试设备('+IP+')')

ScFile = 'D:\\UserData\\Pictures\\MEMU\\screen.png'
RunDir = (sys.path[0]).replace("\\","/")+'/'

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
            ptinfo('Handler'+str(num),'搜索到模拟器窗口'+str(i['title'])+'['+str(i['handle'])+']['+str(i['pos'])+']')
            check=numpy.array(win32gui.GetWindowRect(win32gui.GetDesktopWindow()))>numpy.array(i['pos'])
            if win32gui.IsIconic(i['handle']) : 
                ptinfo(ID,'窗口取消最小化，为保证脚本正常运行，请勿最小化，可使用Win10多桌面放置窗口');
                win32gui.ShowWindow(i['handle'],win32con.SW_RESTORE);
            elif (check==numpy.array([False,False,True,True])).all() : 
                ptinfo(ID,'窗口状态正常，为保证脚本正常运行，请勿最小化，可使用Win10多桌面放置窗口');
            else : ptinfo(ID,'窗口超出本屏幕范围，单显示器可能会影响监视，多显示器可以无视');
            num = num + 1;
    if len(target)==0 : ptinfo('Handler','未检测到MEMU安卓虚拟机窗口');exit();

i=1;
def GetScreen32GUI(ID=0,debug=0) :
    global i;
    start = datetime.datetime.now();
    hWnd = target[ID]['handle']
    while(i) :
        if ID==0 : win32gui.SetWindowPos(hWnd,win32con.HWND_BOTTOM,0,0,960+2,600+34,win32con.SWP_DRAWFRAME)
        if ID==1 : win32gui.SetWindowPos(hWnd,win32con.HWND_BOTTOM,960,0,960+2,600+34,win32con.SWP_DRAWFRAME)
        i=0;
    hWnd = win32gui.FindWindowEx(hWnd,0,'Qt5QWindowIcon','MainWindowWindow');
    hWnd = win32gui.FindWindowEx(hWnd,0,'Qt5QWindowIcon','CenterWidgetWindow');
    hWnd = win32gui.FindWindowEx(hWnd,0,'Qt5QWindowIcon','RenderWindowWindow');

    L, T, R, B = win32gui.GetWindowRect(hWnd)
    width = R - L; height = B - T;
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
    #im_opencv = cv2.resize(im_opencv,(960,600), interpolation=cv2.INTER_NEAREST);
    cv2.imwrite('F:\\Source\\OpenCV-4.3.0\\user\\CV2\\CV2\\1.png',im_opencv)
    if 0 :
        cv2.imshow("im_opencv",im_opencv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd,hWndDC)

    end = datetime.datetime.now();
    if debug : ptinfo(str(end-start)[2:11],'获取WinGUI窗口 '+target[ID]['title']+' 画面');
    return im_opencv

class ResInfo:
    def __init__(self):
        self.cXst=0;self.cYst=0;self.cXed=0;self.cYed=0;
        self.tXst=0;self.tYst=0;self.tXed=0;self.tYed=0;
        self.name='0';

def DefRes(cXc,cYc,cXe,cYe,tXs,tYs,tXe,tYe,name) :
    ID = ResInfo();
    ID.cXst = cXc; ID.cYst = cYc;
    ID.cXed = cXe; ID.cYed = cYe;
    ID.tXst = tXs; ID.tYst = tYs;
    ID.tXed = tXe; ID.tYed = tYe;
    ID.name = name;
    return ID;

pcr_aga = DefRes(   0,   0,   0,   0,0.60,0.88,0.78,0.95,'again.png')
pcr_end = DefRes(   0,   0,   0,   0,0.76,0.90,0.97,0.98,'end.png')
pcr_oks = DefRes(   0,   0,   0,   0,0.50,0.63,0.68,0.71,'ok.png')
pcr_ato = DefRes(   0,   0,   0,   0,   0,   0,   0,   0,'auto.png')
pcr_sto = DefRes(   0,   0,   0,   0,   0,   0,   0,   0,'store.png')

class rdFlag :
    RAW1 = cv2.IMREAD_UNCHANGED;            #原始图像输入
    GRY1 = cv2.IMREAD_GRAYSCALE;            #灰度图像全尺寸输入
    BGR1 = cv2.IMREAD_COLOR;                #BGR彩色图像全尺寸输入
    GRY2 = cv2.IMREAD_REDUCED_GRAYSCALE_2;  #灰度图像W½H½输入
    BGR2 = cv2.IMREAD_REDUCED_COLOR_2;      #BGR彩色图像W½H½输入
    GRY4 = cv2.IMREAD_REDUCED_GRAYSCALE_4;  #灰度图像W¼H¼输入
    BGR4 = cv2.IMREAD_REDUCED_COLOR_4;      #BGR彩色图像W¼H¼输入
    GRY8 = cv2.IMREAD_REDUCED_GRAYSCALE_8;  #灰度图像W⅛H⅛输入
    BGR8 = cv2.IMREAD_REDUCED_COLOR_8;      #BGR彩色图像W⅛H⅛输入 
rdFlag = rdFlag();

class mtFlag :
    SQ  = cv2.TM_SQDIFF;        #平方差匹配
    SQN = cv2.TM_SQDIFF_NORMED; #归一化平方差匹配
    CR  = cv2.TM_CCORR;         #相关匹配
    CRN = cv2.TM_CCORR_NORMED;  #归一化相关匹配
    CE  = cv2.TM_CCOEFF;        #相关系数匹配
    CEN = cv2.TM_CCOEFF_NORMED; #归一化相关系数匹配
mtFlag = mtFlag();

def cv2dp(InArr):
    cv2.imshow("Display", InArr)
    cv2.waitKey(0)

def ptinfo(title,text='') :
    print('\033[1;31;40m'"["+title+"]"+'\033[1;32;40m'" "+str(text));

def Touch(memu,X0,Y0,debug=0):
    TC=random.randint(1,1)
    while TC :
        subprocess.call("adb -s "+memu+" shell input tap "+str(X0)+" "+str(Y0))
        time.sleep(0.05)
        TC = TC - 1
    if debug : ptinfo('ADB.TC',"设备♟ ("+memu+") - 模拟触屏坐标◉ ("+str(X0)+","+str(Y0)+")")

def GetScreenADB(memu,debug=0):
    start = datetime.datetime.now();
    subprocess.call("adb -s "+memu+" shell screencap /sdcard/Pictures/MEMU/screen.png");
    end = datetime.datetime.now();
    if debug : ptinfo(str(end-start)[2:11],'获取屏幕截图▦ '+ScFile);
    return ScFile;

tmp = RunDir+'temp.mjpeg'
def GetMJpegFile(memu,debug=0) : 
    start = datetime.datetime.now();
    ccmd = RunDir + "curl http://"+memu+"/stream.mjpeg -o "+tmp
    curl = subprocess.Popen(ccmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT);
    time.sleep(0.3);
    curl.kill();
    if os.path.exists(tmp) :
        jpeg = cv2.VideoCapture(tmp);
        ret, frame = jpeg.read();
        end = datetime.datetime.now();
        if debug : ptinfo(str(end-start)[2:11],'获取MJEPG流≋ '+"http://"+memu+"/stream.mjpeg 至缓存");
        if ret == True : return frame;
    else : 
        ptinfo('GetMJPEG.ERR','获取MJPEG流出错,缓存文件不存在,调用备用函数');
        return GetMJpegFrame(memu);

def GetMJpegFrame(memu):
    start = datetime.datetime.now();
    stream = urllib.urlopen("http://"+memu+"/stream.mjpeg")
    bytes = stream.read(1024*4096)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        image = bytes[a:b+2]
        bytes = bytes[b+2:]
        screen = cv2.imdecode(numpy.frombuffer(image, dtype=numpy.uint8), rdFlag.BGR1)
    end = datetime.datetime.now();
    #ptinfo(str(end-start)[2:11],'获取MJEPG帧≋ '+"http://"+memu+"/stream.mjpeg");
    return screen

def cv2rd(Var,InMODE=rdFlag.BGR1) :
    if isinstance(Var,str) :
        if Var.rfind('\\') != -1 or Var.rfind('/') != -1 :
            return cv2.imread(Var,InMODE);
        else : 
            return cv2.imread(RunDir+Var,InMODE);
    elif isinstance(Var,numpy.ndarray) :
        if InMODE==rdFlag.BGR1 : return Var;
        if InMODE==rdFlag.GRY1 : return cv2.cvtColor(Var,cv2.COLOR_BGR2GRAY);
        if InMODE==rdFlag.BGR2 : return cv2.resize(Var,(int(Var.shape[1]/2),int(Var.shape[0]/2)), interpolation=cv2.INTER_AREA);
        if InMODE==rdFlag.GRY2 : 
            Var = cv2.cvtColor(Var,cv2.COLOR_BGR2GRAY);
            return cv2.resize(Var,(int(Var.shape[1]/2),int(Var.shape[0]/2)), interpolation=cv2.INTER_AREA);
    else : 
        ptinfo('CV2RD.ERR','输入参数类型异常,仅接受[numpy.ndarray]与[str]');
        return cv2.imread(RunDir+"b0.png",InMODE);

def crop(InArr,InRes) :
    if InRes.cXst==0 : cX0 = 1; 
    else : cX0 = int(InArr.shape[1]*InRes.cXst)
    if InRes.cYst==0 : cY0 = 1;
    else : cY0 = int(InArr.shape[0]*InRes.cXed);
    if InRes.cXed!=0 : cX1 = int(InArr.shape[1]*InRes.cXed);
    else : cX1 = int(InArr.shape[1]);
    if InRes.cYed!=0 : cY1 = int(InArr.shape[0]*InRes.cYed);
    else : cY1 = int(InArr.shape[0]);
    return InArr[cY0:cY1,cX0:cX1];

POS=0;RAT=1;RAW=3;YON=4;MLT=5;thh=0.8;ONE=6;TWO=7;
def cv2mt(InRes,InTempl=ScFile,MODE=POS,InMODE=rdFlag.GRY1,MtMODE=mtFlag.CEN,TDF=ONE) :
    start = datetime.datetime.now();
    #模板匹配
    if TDF==ONE : image = crop(cv2rd(InRes.name,InMODE),InRes);
    if TDF==TWO : image = crop(cv2rd(InRes.name,rdFlag.GRY2),InRes);
    templ = crop(cv2rd(InTempl,InMODE),InRes);
    result = cv2.matchTemplate(image,templ,MtMODE);
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result);
    #数据处理
    if MtMODE==cv2.TM_CCORR or MtMODE==cv2.TM_CCORR_NORMED \
    or MtMODE==cv2.TM_CCOEFF or MtMODE==cv2.TM_CCOEFF_NORMED :
        if InMODE==rdFlag.GRY2 or InMODE==rdFlag.BGR2 :
            RetXY = max_loc[0] * 2, max_loc[1] * 2
        else : RetXY = max_loc
        RetRT = max_val
    if MtMODE==cv2.TM_SQDIFF or MtMODE==cv2.TM_SQDIFF_NORMED :
        if InMODE==rdFlag.GRY2 or InMODE==rdFlag.BGR2 :
            RetXY = min_loc[0] * 2, min_loc[1] * 2
        else : RetXY = min_loc
        RetRT = min_val
    end = datetime.datetime.now();
    if RetRT >=thh :
        if MODE!=YON :
            ptinfo(str(end-start)[2:11],'位图▦ ('+InRes.name+') - 坐标◉ '+str(RetXY)+' - 概率◔ ('+str(int(RetRT*100))+'%)');
    else : return False;
    #数据传回
    if MODE==POS : return max_loc
    if MODE==RAT : return max_val
    if MODE==RAW : return result
    if MODE==YON : return True
    if MODE==MLT : return numpy.where(result >= thh)

def main(memu,Input,templ,Delay=200):
    XY = cv2mt(Input,templ,MODE=POS)        
    if XY != 0 :
        RX=random.randint(int(Input.tXst*960),int(Input.tXed*960))
        RY=random.randint(int(Input.tYst*600),int(Input.tYed*600))
        Touch(memu,RX,RY)
        time.sleep(Delay/1000)
        return 1;
    return 0;

wait=1;t=0;
def run() : 
    global wait,t;
    tmp = GetScreen32GUI(0)
    if cv2mt(pcr_ato,tmp,MODE=YON)==False : 
        main(memu1adb,pcr_end,tmp,random.randint(400,800))
        main(memu1adb,pcr_aga,tmp,random.randint(400,800))
        main(memu1adb,pcr_sto,tmp,random.randint(400,800))
        if main(memu1adb,pcr_oks,tmp,random.randint(1000,2000)) : 
            t = t + 1;
            print(' ');
            ptinfo(str(t),'');
    else : wait = 10;

GetVMhandler();
ADBConnect(memu1adb);
ptinfo('INFO','进入主循环,按住[Alt+MENU]可暂停，按住[Alt+WIN]继续');
print(' ');

state=1;
while(1) : 
    if keyboard.is_pressed('Alt+MENU') : 
        if state!=0 : 
            print('\033[1;31;40m'"[暂停]");
            print(' ');
        state = 0
    if keyboard.is_pressed('Alt+WIN') : 
        if state!=1 : 
            print('\033[1;32;40m'"[继续]");
            print(' ');
        state = 1
    if wait>1 and state==1: 
        wait = wait - 1;
        time.sleep(0.1);
    elif state : run()
