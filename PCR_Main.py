import os
import time

import keyboard

from PCR_Def import PCR
from _PartEnv import *
from _PartEvent import mudevice
from _PartMATCH import matchtl, mt
from _PartWin32 import GetMuHandler

os.system("cls&&title Helper")

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

    def IS(self, flag) : return True if self.flag == flag else False

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

def exec(mu,task:list):
    if not isinstance(task, list) : raise TypeError("task must be a list()")

baseStoreH8 = 0xAF
flagStore = FlagInit(1, '商店', baseStoreH8)
flagStoreNR = FlagInit(2, '商店通常', baseStoreH8)
flagStoreReturn = FlagInit(8, '商店通常', baseStoreH8)

def AutoStore(mu, init=None, Ignore=False) :
    Title = '自动购买'
    h = l.get()
    if init is None : l.set(flagStore, [l.push])
    else : l.set(init, [l.push])
    IgnoreRefreshMANA = True if Ignore else False
    while l.isBase(baseStoreH8) :
        while l.IS(flagStoreNR) :
            if not IgnoreRefreshMANA and not exist(mu, PCR['商店:十万更新'], 0.9) :
                logger.error('风险警告 : 刷新玛娜超过10W 是否无视继续购买一轮 ? 输入Yes回车同意/输入其他退出')
                if 'Yes' == input() :
                    IgnoreRefreshMANA = True
                else :
                    l.set(flagStoreReturn, [l.sw])
                    break

            if 4 <= matchtl(MEMU.GetScreen(), PCR['商店:通常售完'], 0.9, [mt.count, mt.quiet])[0] :
                refresh = PCR['商店:十万更新'] if not IgnoreRefreshMANA else PCR['商店:立刻更新']
                click(mu, refresh, 0.8, param=[1, True, 1], disa=[mt.SELF, 2000])

            click(mu, PCR['商店:选框'], 0.8, param=[1, True, 1])

            if not exist(mu, PCR['商店:选框'], 0.9) :
                click(mu, PCR['商店:批量购入'], 0.8, param=[1, True, 1])

            if exist(mu, PCR['商店:购买确认'], 0.9) :
                click(mu, PCR['商店:确认购买'], 0.8, param=[1, True, 1], disa=[mt.SELF, 2000])
                if not exist(mu, PCR['商店:确认购买'], 0.9) :
                    l.set(flagStoreReturn, [l.sw])
                    break

            if exist(mu, PCR['商店:确认重置'], 0.9) :
                click(mu, PCR['商店:确认购买'], 0.8, param=[1, True, 1], disa=[mt.SELF, 2000])

        # PASS 完成返回
        while l.IS(flagStoreReturn) :
            logger.info('%s 完成于[%s]' % (Title, l.note()))
            l.set(h, [l.pop])
            return True

baseExploreH8 = 0xFC
flagExplore = FlagInit(1, '探索', baseExploreH8)
flagExploreEXP = FlagInit(2, '探索经验', baseExploreH8)
flagExploreMANA = FlagInit(3, '探索玛那', baseExploreH8)
flagExploreReturn = FlagInit(8, '探索返回', baseExploreH8)

def AutoExplore(mu, init=None) :
    Title = '探索'
    h = l.get()
    if init is None : l.set(flagExplore, [l.push])
    else : l.set(init, [l.push])
    lock = [0, 0]

    while l.isBase(baseExploreH8) :
        while l.IS(flagExplore) :
            e0 = PCR['探索:零次0/X']
            t0 = PCR['探索:玛那关卡']
            t1 = PCR['探索:经验关卡']
            f1 = PCR['探索:关卡入口']
            if exist(mu, t0, 0.9) and lock[1] == 0 :
                click(mu, t0, 0.8, param=[1, True, 1], visi=[f1, 2000])
                if exist(mu, e0, 0.9) :
                    lock[1] = 1
                    logger.warning('玛娜探索次数不足')
                    click(mu, PCR['通用:返回'], 0.8, param=[1, True, 1], visi=[t0, 2000])
                else :
                    l.set(flagExploreMANA, [l.sw])
                    break
            if exist(mu, t1, 0.9) and lock[0] == 0 :
                click(mu, t1, 0.8, param=[1, True, 1], visi=[f1, 2000])
                if exist(mu, e0, 0.9) :
                    lock[0] = 1
                    logger.warning('经验探索次数不足')
                    click(mu, PCR['通用:返回'], 0.8, param=[1, True, 1], visi=[t1, 2000])
                else :
                    l.set(flagExploreEXP, [l.sw])
                    break
            if lock == [1, 1] :
                l.set(flagExploreReturn, [l.sw])
                break

        while l.IS(flagExploreMANA) :
            click(mu, PCR['探索:关卡入口'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:加'], 2000])
            click(mu, PCR['扫荡:使用'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
            click(mu, PCR['扫荡:扫荡确认'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
            click(mu, PCR['扫荡:扫荡确认'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
            click(mu, PCR['扫荡:跳过完毕'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:前往经验'], 0])
            l.set(flagExploreEXP, [l.sw])
            break

        while l.IS(flagExploreEXP) :
            click(mu, PCR['探索:关卡入口'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:加'], 2000])
            click(mu, PCR['扫荡:使用'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
            click(mu, PCR['扫荡:扫荡确认'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
            click(mu, PCR['扫荡:扫荡确认'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
            click(mu, PCR['扫荡:跳过完毕'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:前往探索'], 0])
            l.set(flagExploreReturn, [l.sw])
            break

        # PASS 完成返回
        while l.IS(flagExploreReturn) :
            logger.info('%s 完成于[%s]' % (Title, l.note()))
            l.set(h, [l.pop])
            return True

baseDungeonH8 = 0xFD
flagDungeon = FlagInit(1, '地下城', baseDungeonH8)
flagDungeonF1 = FlagInit(2, '1F', baseDungeonH8)
flagDungeonF2 = FlagInit(3, '2F', baseDungeonH8)
flagDungeonF3 = FlagInit(4, '3F', baseDungeonH8)
flagDungeonF4 = FlagInit(5, '4F', baseDungeonH8)
flagDungeonF5 = FlagInit(6, '5F', baseDungeonH8)
flaglistDungeonFx = [flagDungeonF1, flagDungeonF2, flagDungeonF3, flagDungeonF4, flagDungeonF5]
flagDungeonReturn = FlagInit(7, '地下城结束', baseDungeonH8)

def AutoDungeon(mu, init=None) :
    Title = '地下城'
    h = l.get()
    if init is None : l.set(flagDungeon, [l.push])
    else : l.set(init, [l.push])
    ByPassBoss = True

    while l.isBase(baseDungeonH8) :
        # PASS 地下城选择与撤退
        while l.IS(flagDungeon) :
            # Note 寻找 {剩余次数0/1} 跳转 -> 次数不足返回
            t0 = PCR['地下城:次数0/1']
            if exist(mu, t0, 0.9) and not exist(mu, PCR['地下城:撤退'], 0.9) :
                logger.warning('地下城次数不足 返回')
                l.set(flagDungeonReturn, [l.sw])
                break

            # Note 寻找 {N/5} 跳转 -> N层
            lx = [PCR['地下城:1/5'], PCR['地下城:2/5'], PCR['地下城:3/5'],
                  PCR['地下城:4/5'], PCR['地下城:5/5']]
            for i in range(len(lx)) :
                if exist(mu, lx[i], 0.975) :
                    l.set(flaglistDungeonFx[i], [l.sw])
                    break

            # Note 寻找 {剩余次数1/1} -> 点击 {地下城EX3} -> 反馈 {区域确认按钮}
            t1 = PCR['地下城:次数1/1']
            t2 = PCR['地下城:EX3']
            f2 = PCR['地下城:确认地域']
            if exist(mu, t1, 0.9) and exist(mu, t2, 0.9) :
                click(mu, t2, 0.8, param=[1, True, 1], visi=[f2, 2000])
                click(mu, f2, 0.8, param=[1, True, 1], disa=[mt.SELF, 2000])

        while l.IS(flagDungeonF1) :
            click(mu, PCR['地下城:1层'], 0.8, param=[1, True, 1], visi=[PCR['战斗:挑战按钮'], 2000])
            JoinLevelNull(mu)
            _visible(mu, PCR['地下城:报酬窗口'], 0.9, timeout=10000)
            click(mu, PCR['地下城:报酬确认'], 0.8, param=[1, True, 1], disa=[mt.SELF, 2000])
            l.set(flagDungeon, [l.sw])

        while l.IS(flagDungeonF2) :
            click(mu, PCR['地下城:2层'], 0.8, param=[1, True, 1], visi=[PCR['战斗:挑战按钮'], 2000])
            JoinLevelNull(mu)
            _visible(mu, PCR['地下城:报酬窗口'], 0.9, timeout=10000)
            click(mu, PCR['地下城:报酬确认'], 0.8, param=[1, True, 1], disa=[mt.SELF, 2000])
            l.set(flagDungeon, [l.sw])

        while l.IS(flagDungeonF3) :
            click(mu, PCR['地下城:3层'], 0.8, param=[1, True, 1], visi=[PCR['战斗:挑战按钮'], 2000])
            JoinLevelNull(mu)
            _visible(mu, PCR['地下城:报酬窗口'], 0.9, timeout=10000)
            click(mu, PCR['地下城:报酬确认'], 0.8, param=[1, True, 1], disa=[mt.SELF, 2000])
            l.set(flagDungeon, [l.sw])

        while l.IS(flagDungeonF4) :
            click(mu, PCR['地下城:4层'], 0.8, param=[1, True, 1], visi=[PCR['战斗:挑战按钮'], 2000])
            JoinLevelNull(mu)
            _visible(mu, PCR['地下城:报酬窗口'], 0.9, timeout=10000)
            click(mu, PCR['地下城:报酬确认'], 0.8, param=[1, True, 1], disa=[mt.SELF, 2000])
            l.set(flagDungeon, [l.sw])

        while l.IS(flagDungeonF5) :
            # Note 寻找 {撤退按钮} -> 点击 {撤退} -> 反馈 {撤退窗口}
            t1 = PCR['地下城:撤退']
            l5 = PCR['地下城:5/5']
            if ByPassBoss and exist(mu, l5, 0.9) :
                click(mu, t1, 0.8, param=[1, True, 1])

            # Note 寻找 {撤退确认按钮} -> 点击 {确认} -> 反馈 {地下城EX3入口}

            f1 = PCR['地下城:撤退窗口']
            t2 = PCR['地下城:撤退确认']
            if exist(mu, f1, 0.9) :
                click(mu, t2, 0.8, param=[1, True, 1], disa=[mt.SELF, 0])
                l.set(flagDungeon, [l.sw])

        # PASS 完成返回
        while l.IS(flagDungeonReturn) :
            logger.info('%s 完成于[%s]' % (Title, l.note()))
            l.set(h, [l.pop])
            return True
    pass

baseLevelH8 = 0xFE
flagLevel0Select = FlagInit(0, '选择关卡', baseLevelH8)
flagLevel0retWait = FlagInit(1, '等待加载', baseLevelH8)
flagLevel1Panel = FlagInit(2, '打开关卡', baseLevelH8)
flagLevel1Conf = FlagInit(3, '配置关卡', baseLevelH8)
flagLevel2Team = FlagInit(4, '配置队伍', baseLevelH8)
flagLevel3Wait = FlagInit(5, '等待结束', baseLevelH8)
flagLevel4Finish = FlagInit(6, '等待结算', baseLevelH8)
flagLevel5Return = FlagInit(7, '关卡返回', baseLevelH8)
flagLevel5Stop = FlagInit(8, '刷图结束', baseLevelH8)

def JoinLevelNull(mu, init=None) :
    Title = '关卡挑战'
    h = l.get()
    if init is None : l.set(flagLevel1Conf, [l.push])
    else : l.set(init, [l.push])
    while l.isBase(baseLevelH8) :
        # PASS L1 关卡面板 画面
        while l.IS(flagLevel1Conf) :
            # Note 寻找 [挑战] 按钮 -> 点击 {挑战} -> 反馈 {队伍编组面板}
            t = PCR['战斗:挑战按钮']
            f = PCR['战斗:队伍编组']
            click(mu, t, 0.8, param=[1, True, 1], visi=[f, 1000])

            # Note 校验 出现 {队伍编组面板} 跳转 -> L2 队伍配置
            if exist(mu, f, 0.9) :
                l.set(flagLevel2Team, [l.sw])
                break

            # Note 寻找 {体力不足标志} -> 暂停等待 手动处理
            e = PCR['战斗:体力不足']
            while True and exist(mu, e, 0.9) :
                print()
                logger.error('体力不足 暂停等待手动处理 在显示关卡挑战面板时 输入\回车继续')
                if input('  ') == '\\' : break

        # PASS L2 队伍配置 画面
        while l.IS(flagLevel2Team) :
            # Note 寻找 {空队伍标志} -> 点击 {我的队伍} -> 反馈 {呼出此编组按钮} \
            #                       -> 点击 [呼出此编组] -> 反馈 {战斗开始按钮}
            f = PCR['战斗:队伍编组']
            c1 = PCR['战斗:空队伍']
            t1 = PCR['战斗:我的队伍']
            f1 = PCR['战斗:使用编组']
            c2 = PCR['战斗:战斗开始']
            f2 = PCR['通用:载入中']

            if exist(mu, f, 0.9) and exist(mu, c1, 0.9) :
                click(mu, t1, 0.8, param=[1, True, 1], visi=[f1, 5000])
                click(mu, f1, 0.8, param=[1, True, 1], visi=[c2, 5000])
            else :
                # Note 寻找 {战斗开始按钮}  -> 点击 {战斗开始} -> 反馈 {自己消失}
                click(mu, c2, 0.8, param=[1, True, 1], disa=[mt.SELF, 5000])

            # Note 校验 出现 {载入中} 跳转 -> L3 正在战斗
            if exist(mu, f2, 0.9) : l.set(flagLevel3Wait, [l.sw])

        # PASS L3 正在战斗 画面
        while l.IS(flagLevel3Wait) :
            # Note 寻找 {自动战斗标志} -> 保持
            n1 = PCR['战斗:自动']
            n2 = PCR['战斗:时间沙漏']
            if exist(mu, n1, 0.9) or exist(mu, n2, 0.9) : continue

            # Note 寻找 {战斗胜利标志} 或 {结算下一步按钮} -> L4 胜利结算
            t1 = PCR['地下城:胜利']
            t2 = PCR['战斗:挑战胜利']
            t3 = PCR['战斗:玩家等级']
            t4 = PCR['战斗:好感度']
            if exist(mu, t1, 0.9) or exist(mu, t2, 0.9) or \
                    exist(mu, t3, 0.9) or exist(mu, t4, 0.9) :
                l.set(flagLevel4Finish, [l.sw])

        # PASS L4 胜利结算 画面
        while l.IS(flagLevel4Finish) :
            # Note 寻找 {结算下一步按钮} -> 点击 {下一步} -> 反馈 {自己消失}
            t1 = PCR['战斗:下一步']
            ret = click(mu, t1, 0.8, param=[1, True, 1], disa=[mt.SELF, 5000])
            # Note 寻找 {获得道具} -> 点击 {获得道具}
            if ret == retNone :
                t1 = PCR['战斗:挑战胜利']
                t2 = PCR['战斗:获得道具']
                click(mu, t1, 0.8, param=[2, True, 5])
                click(mu, t2, 0.8, param=[2, True, 5])
            # Note 寻找 {限定商店窗口} -> 点击 {取消按钮} -> 反馈 {自己消失}
            n1 = PCR['战斗:限定商店']
            t1 = PCR['战斗:商店取消']
            if exist(mu, n1, 0.9) :
                click(mu, t1, 0.8, param=[1, True, 1], disa=[mt.SELF, 4000])

            # Note 校验 出现 {载入中} 跳转 -> 完成返回
            n1 = PCR['通用:载入中']
            if exist(mu, n1, 0.9) : l.set(flagLevel5Return, [l.sw])

        # PASS 完成返回
        while l.IS(flagLevel5Return) or keyboard.is_pressed('Alt+CTRL') :
            logger.info('%s 完成于[%s]' % (Title, l.note()))
            l.set(h, [l.pop])
            return True

    pass  # while this

def AutoNextLevel(mu, init=None) :
    Title = '关卡'
    h = l.get()
    if init is None : l.set(flagLevel0Select, [l.push])
    else : l.set(init, [l.push])

    while l.isBase(baseLevelH8) :
        # PASS 关卡列表 下一关
        while l.IS(flagLevel0Select) :
            # Note 寻找 {下一关标志} -> 点击 {下一关-偏移} -> 反馈 {关卡挑战按钮}
            t1 = PCR['战斗:下一关']
            f1 = PCR['战斗:挑战按钮']
            e1 = PCR['战斗:下一关备用']
            click(mu, t1, 0.9, param=[1, True, 1], visi=[f1, 500])

            # Note 校验 出现 {关卡挑战按钮} 跳转 -> 关卡挑战
            if exist(mu, f1, 0.9) :
                l.set(flagLevel1Panel, [l.sw])
                break

            # Note 寻找 {下一关备用标志} -> 点击 {备用偏移}
            if not exist(mu, t1, 0.9) :
                mat = mu.GetScreen()
                xy = exist(mu, e1, 0.9, retxy=True)
                if xy != retNone and type(xy).__name__ != 'bool' :
                    x, y = xy[0] - 50, xy[1] + 60
                    crop = mat[y :y + 90, x :x + 100]
                    if xyFalse != matchtl(crop, PCR['战斗:通关星'], 0.975) :
                        logger.warning('无(未达成一星/两星/三星)未通过的关卡 终止返回')
                        l.set(flagLevel5Stop, [l.sw])
                    else :
                        click(mu, e1, 0.9, param=[1, True, 1], visi=[f1, 1000])

            # Note 寻找 {剧情弹窗标志} -> 点击 {取消/关闭} -> 反馈 {自己消失}
            t2 = PCR['战斗:挑战取消']
            t3 = PCR['任务:关闭']
            if not exist(mu, t1, 0.9) and not exist(mu, f1, 0.9) :
                click(mu, t2, 0.8, param=[1, True, 1], disa=[mt.SELF, 4000])
                click(mu, t3, 0.8, param=[1, True, 1], disa=[mt.SELF, 4000])

        # PASS 关卡挑战
        while l.IS(flagLevel1Panel) :
            # Note 开始挑战 等待结束 -> 关卡返回
            JoinLevelNull(mu)
            l.set(flagLevel0retWait, [l.sw])

        # PASS 关卡返回
        while l.IS(flagLevel0retWait) :
            # Note 寻找 {普通难度标志} -> 关卡列表 下一关
            if exist(mu, PCR['主线:普通'], 0.9) : l.set(flagLevel0Select, [l.sw])

        # PASS 终止
        while l.IS(flagLevel5Stop) or keyboard.is_pressed('Alt+CTRL') :
            logger.info('%s 完成于[%s]' % (Title, l.note()))
            l.set(h, [l.pop])
            return True

    pass  # while this

baseLoginH8 = 0xFF
flagDefault = FlagInit(1, 'PCR', baseLoginH8)
flagRunApp = FlagInit(2, '主程序', baseLoginH8)
flagLogin1Touch = FlagInit(3, '登录界面', baseLoginH8)
flagLogin2DailyMA = FlagInit(4, '每日盖章', baseLoginH8)
flagLogin3Special = FlagInit(5, '特色活动', baseLoginH8)
flagLogin4Notice = FlagInit(6, '通知预告', baseLoginH8)
flagEvent = FlagInit(7, '活动', baseLoginH8)
flagNotice = FlagInit(8, '通告', baseLoginH8)
flagSpLanDeSuoEr = FlagInit(9, '通告', baseLoginH8)

flagIndex = FlagInit(0xF102, '主页')
flagAdventure = FlagInit(0xF104, '冒险')

def Login(mu, init=None) :
    Title = '登录'
    h = l.get()
    if init is None : l.set(flagRunApp)
    else : l.set(init)

    while l.isBase(baseLoginH8) :
        # PASS 游戏主程序载入
        while l.IS(flagRunApp) :
            # Note 寻找 {点击屏幕 登陆游戏} -> 点击登录界面
            if exist(mu, PCR['登录:点击屏幕'], 0.9) : l.set(flagLogin1Touch, [l.push])

        # PASS 点击登录界面
        while l.IS(flagLogin1Touch) :
            # Note 寻找 {点击屏幕 登陆游戏} -> 点击 {点击屏幕} -> 反馈 {自己消失}
            click(mu, PCR['登录:点击屏幕'], 0.8, param=[1, True, 1], disa=[mt.SELF, 5000])

            # Note 寻找 {签到跳过按钮} 跳转 -> 每日签到界面
            if exist(mu, PCR['登录:跳过'], 0.9) :
                l.set(flagLogin2DailyMA, [l.sw])
                break

            # Note 寻找 {通知窗口} 跳转 -> 主界面通知窗口
            if exist(mu, PCR['通告:通知活动'], 0.9) :
                l.set(flagLogin4Notice, [l.sw])
                break

            if exist(mu, PCR['兰德索尔杯:选择角色'], 0.9) :
                l.set(flagSpLanDeSuoEr, [l.sw])
                break

        # PASS 当日首次登录
        while l.IS(flagLogin2DailyMA) :
            # Note 寻找 {签到跳过按钮} -> 点击 {跳过按钮} -> 反馈 {自己消失}
            click(mu, PCR['登录:跳过'], 0.8, param=[1, True, 1], disa=[mt.SELF, 5000])

            # Note 寻找 {通知窗口} 跳转 -> 主界面通知窗口
            if exist(mu, PCR['通告:通知活动'], 0.9) :
                l.set(flagLogin4Notice, [l.sw])
                break

            if exist(mu, PCR['兰德索尔杯:选择角色'], 0.9) :
                l.set(flagSpLanDeSuoEr, [l.sw])
                break

        # PASS 兰德索尔杯
        while l.IS(flagSpLanDeSuoEr) :
            # Note 寻找 {选择角色} -> 点击 {随机旗帜} -> 点击 {开始}
            if exist(mu, PCR['兰德索尔杯:选择角色'], 0.9) :
                t = PCR['兰德索尔杯:旗帜'][random.randint(0, 3)]
                w = PCR['兰德索尔杯:开始']
                click(mu, t, 0.8, param=[1, True, 1], visi=[w, 5000])
                click(mu, w, 0.8, param=[1, True, 1], disa=[mt.SELF, 5000])

            # Note 寻找 {跳过} -> 点击 {随机旗帜} -> 点击 {开始}
            t = PCR['兰德索尔杯:跳过']
            f = PCR['兰德索尔杯:结果']
            click(mu, t, 0.8, param=[1, True, 1], visi=[f, 5000])

            if exist(mu, f, 0.9) :
                click(mu, f, 0.8, param=[1, True, 1], disa=[mt.SELF, 5000])
                if not exist(mu, f, 0.9) :
                    l.set(flagLogin4Notice, [l.sw])
                    break

            # Note 寻找 {通知窗口} 跳转 -> 主界面通知窗口
            if exist(mu, PCR['通告:通知活动'], 0.9) :
                l.set(flagLogin4Notice, [l.sw])
                break

        # PASS 主界面通知窗口
        while l.IS(flagLogin4Notice) :
            # Note 寻找 {通知/活动标志} -> 点击 {关闭按钮} -> 反馈 {自己消失}
            if exist(mu, PCR['通告:通知活动'], 0.9) :
                click(mu, PCR['通告:关闭按钮'], 0.8, param=[1, True, 1], disa=[mt.SELF, 1000])
                # Note 寻找 {导航主页按钮} 跳转 -> 登陆完成
                while not exist(mu, PCR['导航:主页'], 0.9) : pass
                l.set(flagIndex, [l.sw])

        # PASS 登陆完成
        while l.IS(flagIndex) or keyboard.is_pressed('Alt+CTRL') :
            logger.info('%s 完成于[%s]' % (Title, l.note()))
            l.set(h, [l.pop])
            return True

    pass  # while this

def main() :
    # Login(MEMU)
    # AutoNextLevel(MEMU)
    AutoDungeon(MEMU)
    # AutoExplore(MEMU)
    # AutoStore(MEMU, flagStoreNR,Ignore=True)
    exit()
    pass

logger.warning('进入主循环,按住[Alt+MENU]可暂停，按住[Alt+WIN]继续\n')

GetMuHandler()
MEMU = mudevice("127.0.0.1:21503", "VM", "/dev/input/event6")
MEMU.connect()

l = auto = FlagCtrl(flag=flagDefault, pause=False)
l.set(flagRunApp, [l.root])

if __name__ == '__main__' :
    while True :
        if keyboard.is_pressed('Alt+MENU') :
            if not auto.pause : print('\033[1;31;40m'"[暂停]\n")
            auto.pause = True
        if keyboard.is_pressed('Alt+WIN') :
            if auto.pause : print('\033[1;32;40m'"[继续]\n")
            auto.pause = False
        if not auto.pause :
            main()
