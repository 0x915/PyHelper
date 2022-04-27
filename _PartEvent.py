#	ASUS_Z01QD:/ # getevent
#
#		add device 4: /dev/input/event0 = name : "Power Button"
#		add device 3: /dev/input/event1 = name : "Sleep Button"
#		add device 6: /dev/input/event2 = name : "AT Translated Set 2 keyboard"
#		add device 5: /dev/input/event3 = name : "ImExPS/2 Generic Explorer Mouse"
#		add device 7: /dev/input/event4 = name : "MemuHyperv USB Tablet"
#		add device 2: /dev/input/event5 = name : "MemuHyperv mouse integration"
#		add device 1: /dev/input/event6 = name : "User Input"
#
#		could not get driver version for /dev/input/mouse2, Not a typewriter
#		could not get driver version for /dev/input/mouse0, Not a typewriter
#		could not get driver version for /dev/input/mice  , Not a typewriter
#		could not get driver version for /dev/input/mouse1, Not a typewriter

#         "sendevent /dev/input/event6 00 00 0000",  #---------------
#         "sendevent /dev/input/event6 03 53 1730",  # 0x35 PointerX
#         "sendevent /dev/input/event6 03 54 1143",  # 0x36 PointerY
#         "sendevent /dev/input/event6 00 00 0000",  #---------------

#         "sendevent /dev/input/event6 00 00 00  ",  #---------------
#         "sendevent /dev/input/event6 03 48 10  ",  # 0x30 PressNum
#         "sendevent /dev/input/event6 03 57 00  ",  # 0x39 00000000
#         "sendevent /dev/input/event6 00 00 00  ",  #---------------

#         "sendevent /dev/input/event6 00 00 00  ",  #---------------
#         "sendevent /dev/input/event6 03 48 00  ",  # 0x30 00000000
#         "sendevent /dev/input/event6 03 57 -1  ",  # 0x39 FFFFFFFF
#         "sendevent /dev/input/event6 00 00 00  "]  #---------------
import subprocess
import time

from _PartEnv import *
from _PartWin32 import GetVMScreen

class mudevice :

    def __init__(self, addr, title, inputdev="/dev/input/event6") :
        self.title = title
        self.device = addr
        self.inputdev = inputdev
        self.touchcount = 0
        logger.info("定义设备 [%s] [%s] [%s]" % (self.title, self.device, self.inputdev))

    def connect(self, string='') :
        subprocess.call("adb connect " + str(self.device), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info("连接设备 [%s] [%s]" % (self.title, self.device))
        print(string)

    def command(self, string) :
        # print("adb -s %s shell %s"%(self.device,string))
        try :
            subprocess.call("adb -s %s shell %s" % (self.device, string),
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, )
        except :
            self.connect()
            time.sleep(1)
            subprocess.call("adb -s %s shell %s" % (self.device, string),
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, )

    def sendevent(self, EventList) :
        for Event in EventList :
            self.command(Event)

    def inputTouch(self, xy, endSleep=1) :
        if xy == (0,0) : return False
        tX, tY = xy
        self.touchcount += 1
        if self.touchcount >= 16 : self.touchcount = 0
        self.command('input tap %s %s' % (tX, tY))
        logger.debug("调试输入 " + str((tX, tY)) + " 计数 " + str(self.touchcount))
        time.sleep(endSleep / 1000)

    def eventTouch(self, xy, pressTime=0, repeat=1, endSleep=0.001) :
        tX, tY = xy
        for I in range(repeat) :
            self.touchcount += 1
            if self.touchcount >= 16 : self.touchcount = 0

            logger.debug("事件输入 " + str((tX, tY, pressTime)) + " 计数 " + str(self.touchcount))

            EventList = list()  # 按下
            EventList.append("sendevent " + self.inputdev + " 03 53 " + str(tX))
            EventList.append("sendevent " + self.inputdev + " 03 54 " + str(tY))
            EventList.append("sendevent " + self.inputdev + " 00 00 0000")
            self.sendevent(EventList)

            # time.sleep(random.randint(int(1),int(10))/1000)

            EventList = list()  # 计数
            EventList.append("sendevent " + self.inputdev + " 03 48 " + str(self.touchcount))
            EventList.append("sendevent " + self.inputdev + " 03 57 00")
            EventList.append("sendevent " + self.inputdev + " 00 00 00")
            self.sendevent(EventList)

            time.sleep(random.randint(int(pressTime * 0.8), int(pressTime * 1.2)) / 1000)

            EventList = list()  # 抬起
            EventList.append("sendevent " + self.inputdev + " 03 48 00")
            EventList.append("sendevent " + self.inputdev + " 03 57 -1")
            EventList.append("sendevent " + self.inputdev + " 00 00 00")
            self.sendevent(EventList)

            time.sleep(random.randint(int(1), int(10)) / 1000)

            time.sleep(endSleep)

    def GetScreen(self): return GetVMScreen(title=self.title)

if __name__ == '__main__' :
    pass
