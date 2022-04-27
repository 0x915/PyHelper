import numpy
import random
import datetime
import urllib.request as urllib
from HelperCorePublic import *

def GetMJpegFrame(memu,debug=0):
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
    if debug : ptinfo(str(end-start)[2:11],'获取MJEPG帧≋ '+"http://"+memu+"/stream.mjpeg");
    return screen
