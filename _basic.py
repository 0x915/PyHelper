import time

from _PartEnv import *
from _PartMATCH import matchtl, mt

class FlagCtrl :
    sw = 0
    pop = 1
    push = 2
    root = 3
    quite = 4

    def __init__(self, flag, pause) :
        self.flag = flag
        self.pause = pause
        self.layer = list()

    def get(self) : return self.flag

    def note(self) : return self.flag.note

    def isBase(self, base) : return self.flag.flag >> 8 == base

    def set(self, flag, param=None) :
        if param is None : param = [self.sw]
        if type(param).__name__ != 'list' : param = [param]

        if self.flag == flag :
            logger.warning('  flagSet %s == %s ???  ' % (self.flag.note, flag.note))
        else :
            if self.pop in param :
                logstr = 'GoBack', '%s ←' % flag.note
                self.layer = self.layer[:-1]
            elif self.push in param :
                logstr = 'GoTo', '→ %s' % flag.note
                self.layer.append(flag.note)
            elif self.sw in param :
                logstr = 'Move', '%s → %s' % (self.flag.note, flag.note)
                self.layer[-1] = [flag.note]
            elif self.root in param :
                logstr = 'Root', '%s' % flag.note
                self.layer = [flag.note]
            else : logstr = 'Update'
            logger.debug('  flag%s  %s  ' % (logstr[0], logstr[1]))
            self.flag = flag

        if self.quite in param :
            logger.debug('  ' + str(self.layer)
                         .replace("'", '')
                         .replace(', ', '/')
                         .replace('[', '')
                         .replace(']', ''))

    def IS(self, flag) : return True if self.flag == flag or self.flag.note == flag else False

class FlagInit :

    def __init__(self, flagNum, flagNote='L', base=0) :
        self.flag = base << 8 | flagNum
        self.note = flagNote

    def __call__(self) : return self.flag

#   等待出现   < 超时timeout 保持时间holdtime >
def _visible(mu, tlist, threshold=0.8, timeout=0, holdtime=0) :
    """
    等待模板图像出现 (超时返回)

    :param mu: 模拟器对象
    :param tlist: 模板组列表
    :param threshold: 匹配阈值
    :return: 成功retFind 失败retNone
    """
    if type(tlist) != type(list()) : tlist = [tlist]

    for tl in tlist :
        if type(tl).__name__ != typeTL :
            logger.error('_visible 模板类型异常 %s ≠ input(%s)' % (typeTL, type(tl)))
            exit()

    # 等待超时控制
    start_time = datetime.datetime.now()
    break_time = start_time + datetime.timedelta(seconds=abs(timeout + 1) / 1000)

    logger.info('等待出现[%s] 超时等待%6sms' % (tlist[0].text, timeout if timeout != 0 else '∞'))

    for tl in tlist :
        while True :  # while find
            if xyFalse != matchtl(mu.GetScreen(), tl, threshold, [mt.quiet]) :
                logger.info('出现完成{%s} %6sms ' % (tl.text, str((datetime.datetime.now() - start_time).microseconds)[:-3]))
                if holdtime != 0 :
                    time.sleep(abs(holdtime) / 1000)
                    if xyFalse != matchtl(mu.GetScreen(), tl, threshold, [mt.quiet]) : pass
                    else :
                        logger.info('保持失败[%s]' % tlist[0].text)
                        return retHoldFail
                return retFind
            if timeout != 0 and datetime.datetime.now().__gt__(break_time) :
                logger.warning('出现超时{%s}' % tl.text)
                return retTimeout
    return retNone

#   等待消失   < 超时timeout 保持时间holdtime >
def _disappear(mu, tlist, threshold=0.8, timeout=0, holdtime=0) :
    """
    等待模板图像消失 (超时返回)

    :param mu: 模拟器对象
    :param tlist: 模板组列表
    :param threshold: 匹配阈值
    :param timeout: 超时毫秒值
    :return: 失败retFind 成功retNone 超时retTimeout
    """

    if type(tlist) != type(list()) : tlist = [tlist]

    for tl in tlist :
        if type(tl).__name__ != typeTL :
            logger.error('_disappear 模板类型异常 %s ≠ input(%s)' % (typeTL, type(tl)))
            exit()

    # 等待超时控制
    start_time = datetime.datetime.now()
    break_time = start_time + datetime.timedelta(seconds=abs(timeout + 1) / 1000)

    logger.info('等待消失[%s] 超时等待%6sms' % (tlist[0].text, timeout if timeout != 0 else '∞'))

    for tl in tlist :
        while True :  # while find
            if xyFalse == matchtl(mu.GetScreen(), tl, threshold, [mt.quiet]) :
                logger.info('消失完成{%s} %6sms ' % (tl.text, str((datetime.datetime.now() - start_time).microseconds)[:-3]))
                if holdtime != 0 :
                    time.sleep(abs(holdtime) / 1000)
                    if xyFalse == matchtl(mu.GetScreen(), tl, threshold, [mt.quiet]) : pass
                    else :
                        logger.info('保持失败[%s]' % tlist[0].text)
                        return retHoldFail
                return retFind
            if timeout != 0 and datetime.datetime.now().__gt__(break_time) :
                logger.warning('消失超时 %6sms' % tl.text)
                return retTimeout
        pass  # while this

    return retNone

#   找到点击   < param[次数,随机,延迟] disa[_disappear()] visi[_visible()] >
def click(mu, tlist, threshold=0.8, param=None, disa=None, visi=None, endsleep=10) :
    """
     点击模板图像 (等待响应返回 + 超时返回)

     param 点击参数 [点击次数=int,区域随机=bool,点击间隔毫秒=int]
     　　　　　　　　随即区域 使用模板对象.FB()保存的区域
     　　　　　　　　间隔毫秒 每次点击指令发出后暂停的时间

     disa 消失响应参数 [模板类=class,超时毫秒数=int,保持时间=int]
     visi 可见响应参数 [模板类=class,超时毫秒数=int,保持时间=int]
     　　　　  　　 　　超时毫秒 在设定时间后强制结束返回
     　　　　  　　 　　保持时间 在设定时间后重新进行匹配

    :param mu: 模拟器对象
    :param tlist: 模板组列表
    :param threshold: 匹配阈值
    :param param: 点击参数
    :param disa: 消失响应参数
    :param visi: 可见响应参数
    :param endsleep: 返回延迟
    :return: 成功retFind 失败retNone 超时retTimeout
    """

    if type(tlist).__name__ != 'list' : tlist = [tlist]
    if type(param).__name__ != 'list' : param = []
    if type(disa).__name__ != 'list' : disa = []
    if type(visi).__name__ != 'list' : visi = []

    for tl in tlist :
        if type(tl).__name__ != typeTL :
            logger.error('click 模板类型异常 %s ≠ input(%s)' % (typeTL, type(tl)))
            exit()

    repeat = param[0] if len(param) >= 1 else 1
    rand = param[1] if len(param) >= 2 else False
    ms = param[2] if len(param) >= 3 else 10

    for tl in tlist :
        XY = matchtl(mu.GetScreen(), tl, threshold, [])
        if XY != xyFalse :
            if tl.FB == fbNone : return retFind

            for i in range(repeat) :
                if rand and tl.FB == fbSelf :
                    dx = int(tl.width / 2)
                    dy = int(tl.width / 2)
                    XY = GetFBXY(XY, tl=[-dx, -dy, +dx, +dy])
                elif rand : XY = GetFBXY(XY, tl=tl)
                mu.inputTouch(XY)
                time.sleep(random.randint(int(ms * 0.5), int(ms * 1.5)) / 1000)
            pass  # for repeat

            if disa :
                dtl = disa[0] if len(disa) >= 1 else None
                if dtl == mt.SELF : dtl = tl
                timeout = disa[1] if len(disa) >= 2 else 0
                holdtime = disa[2] if len(disa) >= 3 else 0
                _disappear(mu, dtl, threshold, timeout, holdtime)

            if visi :
                vtl = visi[0] if len(visi) >= 1 else None
                if vtl == mt.SELF : vtl = tl
                timeout = visi[1] if len(visi) >= 2 else 0
                holdtime = visi[2] if len(visi) >= 3 else 0
                _visible(mu, vtl, threshold, timeout, holdtime)

            time.sleep(abs(endsleep) / 1000)
            return retFind

        pass  # if xyTrue

    pass  # for tlist

    return retNone

#   是否存在   < mu[class.mudevice] tlist[class.definetl] >
def exist(mu, tlist, threshold=0.8, quiet=mt.quiet, retxy=False) :
    if type(tlist) != type(list()) : tlist = [tlist]

    for tl in tlist :
        if type(tl).__name__ != typeTL :
            logger.error('exist 模板类型异常 %s ≠ input(%s)' % (typeTL, type(tl)))
            exit()
        xy = matchtl(mu.GetScreen(), tl, threshold, [quiet])
        if xyFalse != xy :
            if retxy : return int(xy[0] / cvScale), int(xy[1] / cvScale)
            return retFind
    return retNone

# def exec(mu, task: list) :
#     if not isinstance(task, list) : raise TypeError("task must be a list()")
