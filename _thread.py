from _public import *
from _PartMatch import *
from ctypes import pythonapi,py_object

os.system('cls')

class _Thread(threading.Thread) :
   def __init__(self,name,temp) :
      super().__init__()
      self.__name = name
      self.__temp = temp
      self.__flag = threading.Event()
      self.__flag.set()
   def pause(self) : 
      logger.warning("Thread ID[%s] NAME[%s] ▥ 暂停  ... "%(self.ident,self.__name))
      self.__flag.clear()
   def resume(self) : 
      logger.warning("Thread ID[%s] NAME[%s] ▤ 恢复 ... "%(self.ident,self.__name))
      self.__flag.set()
   def stop(self) : 
      ret = pythonapi.PyThreadState_SetAsyncExc(self.ident, py_object(SystemExit))
      if ret == 0 : 
         logger.error("ValueError Invalid Thread ID")
      elif ret != 1 : 
         pythonapi.PyThreadState_SetAsyncExc(self.ident, 0)
         logger.error("SystemError PyThreadState_SetAsyncExc Failed")
         time.sleep(0.1);
      elif ret == 1 :
         logger.warning("线程 ID[%s] NAME[%s] ☒ 停止 !!! "%(self.ident,self.__name));
         time.sleep(0.1);
   def run(self) : 
      logger.info("线程 ID[%s] NAME[%s] ☐ 启动 ... " % (self.ident, self.__name))
      while True : 
         self.__flag.wait()
         cv2mt(image,self.__temp)


image = cv2.imread("./__0.jpg")

def main() :
   Thread = []
   a = _Thread(name='1',temp=t1)
   Thread.append(a)
   b = _Thread(name='2',temp=t2)
   Thread.append(b)
   c = _Thread(name='3',temp=t3)
   Thread.append(c)
   Thread[0].start()
   Thread[1].start()
   Thread[2].start()
   print(" ")
   time.sleep(1)
   Thread[0].pause()
   Thread[1].pause()
   Thread[2].pause()
   print(" ")
   time.sleep(2)
   Thread[0].stop()
   Thread[1].stop()
   Thread[2].stop()
   exit()
if __name__ == '__main__':
    main()
