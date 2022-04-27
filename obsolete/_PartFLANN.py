from _PartEnv import *

def FLANN(screen,target,info="",debug=False) :
    
    start = datetime.datetime.now();

    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(screen,None)
    kp2, des2 = sift.detectAndCompute(target,None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    good=list()
    for m,n in matches : 
        if m.distance < 0.7*n.distance : good.append(m)

    if len(good) < 10 : return (False,False)

    ntmp=list();i=0
    src_pts = numpy.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    for pt1 in src_pts : 
        a = pt1[0].astype(int);c = 0
        for count in range(i,len(src_pts)) : 
            b = src_pts[count][0].astype(int)
            d = numpy.linalg.norm(a-b)
            if d < 32 : c += 1
        if c > 5 : 
            ntmp.append(a)
        i += 1
        
    if len(ntmp) < 5 : return (False,False)
    
    result = numpy.average(ntmp, axis=0).astype(int)
    end = datetime.datetime.now();
    ms = str((end-start).microseconds)[:-3]
    logger.info('FLANN %s%s◔ %s 耗时(%sms)' \
                 % (info,str(result).replace("  ", ","),len(ntmp),\
                  str((end-start).microseconds)[:-3]))
        
    if debug :
        for point in ntmp : dbg = cv2.circle(screen, (point[0],point[1]), 1, (0, 0, 255),2)
        dbg = cv2.circle(dbg, (result[0],result[1]), 4, (0, 255, 0),8)
        cv2.imshow("DebugFLANN",dbg)
        cv2.waitKey(1)
    
    return int(result[0] * cvScale), int(result[1] * cvScale)



if __name__ == '__main__':
    from _PartWin32 import *
    GetMuHandler()
    XYG = ".\\PCR1280x720\\XYG.png"
    while True : 
        #cv2.imwrite("out.jpg", GetVMScreen());exit()
        FLANN(GetVMScreen(),cv2.imread(XYG,0),"下一关",debug=True)
