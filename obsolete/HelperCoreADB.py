import time
import random
import datetime
import subprocess

from HelperCorePublic import *

ScFile = 'D:\\UserData\\Pictures\\MEMU\\screen.png'

def ADBConnect(IP) :
    if ':' in IP and '.' in IP :
        subprocess.call("adb connect "+IP,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ptinfo('ADB','连接调试设备('+IP+')')

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

def GetScreenSky(memu,debug=0):
    start = datetime.datetime.now();
    subprocess.call("adb -s "+memu+" shell screencap /sdcard/Android/sky.png");
    subprocess.call("adb -s "+memu+" pull /sdcard/Android/sky.png");
    end = datetime.datetime.now();
    if debug : ptinfo(str(end-start)[2:11],'获取屏幕截图▦ '+ScFile);
    return ScFile;