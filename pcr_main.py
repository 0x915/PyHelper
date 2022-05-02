import os

import keyboard

from pcr_tl import PCR
from _public import *
from _android import mudevice
from _match import matchtl, mt
from _platform import GetMuHandler
from _basic import FlagCtrl, FlagInit, _visible, click, exist

os.system("cls&&title Helper")

class AutoStore :
    base = 0xAF
    flag = {
        '商店'   : FlagInit(1, '商店', base),
        '通常'   : FlagInit(2, '商店通常', base),
        '商店返回' : FlagInit(8, '商店返回', base),
    }

    @classmethod
    def main(cls, mu, init=None, Ignore=False) :
        Title = '自动购买'
        h = l.get()
        if init is None : l.set(cls.flag['商店'], [l.push])
        else : l.set(init, [l.push])
        IgnoreRefreshMANA = True if Ignore else False
        while l.isBase(cls.base) :
            while l.IS(cls.flag['通常']) :
                if not IgnoreRefreshMANA and not exist(mu, PCR['商店:十万更新'], 0.9) :
                    logger.error('风险警告 : 刷新玛娜超过10W 是否无视继续购买一轮 ? 输入Yes回车同意/输入其他退出')
                    if 'Yes' == input() :
                        IgnoreRefreshMANA = True
                    else :
                        l.set(cls.flag['商店返回'])
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
                        l.set(cls.flag['商店返回'])
                        break

                if exist(mu, PCR['商店:确认重置'], 0.9) :
                    click(mu, PCR['商店:确认购买'], 0.8, param=[1, True, 1], disa=[mt.SELF, 2000])

            # PASS 完成返回
            while l.IS(cls.flag['商店返回']) :
                logger.info('%s 完成于[%s]' % (Title, l.note()))
                l.set(h, [l.pop])
                return True

class AutoExplore :
    base = 0xFC
    flag = {
        '探索'   : FlagInit(1, '探索', base),
        '经验'   : FlagInit(2, '探索经验', base),
        '玛那'   : FlagInit(3, '探索玛那', base),
        '探索返回' : FlagInit(8, '探索返回', base),
    }

    @classmethod
    def main(cls, mu, init=None) :
        Title = '探索'
        h = l.get()
        if init is None : l.set(cls.flag['探索'], [l.push])
        else : l.set(init, [l.push])
        lock = [0, 0]

        while l.isBase(cls.base) :
            while l.IS(cls.flag['探索']) :
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
                        l.set(cls.flag['玛那'])
                        break
                if exist(mu, t1, 0.9) and lock[0] == 0 :
                    click(mu, t1, 0.8, param=[1, True, 1], visi=[f1, 2000])
                    if exist(mu, e0, 0.9) :
                        lock[0] = 1
                        logger.warning('经验探索次数不足')
                        click(mu, PCR['通用:返回'], 0.8, param=[1, True, 1], visi=[t1, 2000])
                    else :
                        l.set(cls.flag['经验'])
                        break
                if lock == [1, 1] :
                    l.set(cls.flag['探索返回'])
                    break

            while l.IS(cls.flag['玛那']) :
                click(mu, PCR['探索:关卡入口'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:加'], 2000])
                click(mu, PCR['扫荡:使用'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
                click(mu, PCR['扫荡:扫荡确认'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
                click(mu, PCR['扫荡:扫荡确认'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
                click(mu, PCR['扫荡:跳过完毕'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:前往经验'], 0])
                l.set(cls.flag['经验'])
                break

            while l.IS(cls.flag['经验']) :
                click(mu, PCR['探索:关卡入口'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:加'], 2000])
                click(mu, PCR['扫荡:使用'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
                click(mu, PCR['扫荡:扫荡确认'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
                click(mu, PCR['扫荡:扫荡确认'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:跳过完毕'], 0])
                click(mu, PCR['扫荡:跳过完毕'], 0.8, param=[1, True, 1], visi=[PCR['扫荡:前往探索'], 0])
                l.set(cls.flag['探索返回'])
                break

            # PASS 完成返回
            while l.IS(cls.flag['探索返回']) :
                logger.info('%s 完成于[%s]' % (Title, l.note()))
                l.set(h, [l.pop])
                return True

class AutoDungeon :
    base = 0xFD
    flag = {
        '默认' : FlagInit(1, '地下城关卡', base),
        '一层' : FlagInit(2, '1F', base),
        '二层' : FlagInit(3, '2F', base),
        '三层' : FlagInit(4, '3F', base),
        '四层' : FlagInit(5, '4F', base),
        '五层' : FlagInit(6, '5F', base),
        '撤退' : FlagInit(7, '撤退', base),
        '结束' : FlagInit(8, '地下城结束', base),
    }
    flagFX = [flag['一层'], flag['二层'], flag['三层'], flag['四层'], flag['五层']]
    temlFX = [PCR['地下城:1/5'], PCR['地下城:2/5'], PCR['地下城:3/5'], PCR['地下城:4/5'], PCR['地下城:5/5']]

    ByPassBoss = True

    @classmethod
    def main(cls, mu, init=None) :
        Title = '地下城'
        h = l.get()

        if init is None : l.set(cls.flag['默认'], [l.push])
        else : l.set(init, [l.push])

        ##################################################

        while l.isBase(cls.base) :
            # PASS 地下城选择与撤退
            while l.IS(cls.flag['默认']) :
                # Note 页面：地下城选择地域
                #      寻找 {剩余次数0/1} 跳转 -> 次数不足返回
                if exist(mu, PCR['地下城:次数0/1'], 0.9) and \
                        not exist(mu, PCR['地下城:撤退'], 0.9) :
                    logger.warning('地下城次数不足 返回')
                    l.set(cls.flag['结束'])
                    break

                # Note 页面：地下城选择地域 + 确认地域
                #      寻找 {剩余次数1/1} -> 点击 {地下城EX3} -> 反馈 {区域确认按钮}
                if exist(mu, PCR['地下城:次数1/1'], 0.9) and exist(mu, PCR['地下城:EX3'], 0.9) :
                    click(mu, PCR['地下城:EX3'], 0.8, param=[1, True, 1],
                          visi=[PCR['地下城:确认地域'], 2000])
                    click(mu, PCR['地下城:确认地域'], 0.8, param=[1, True, 1],
                          disa=[mt.SELF, 2000])

                # Note 页面：地下城地域地图内
                #      寻找 {N/5} -> 跳转 {N层}
                for i in range(len(cls.flagFX)) :
                    if exist(mu, cls.temlFX[i], 0.975) :
                        l.set(cls.flagFX[i])
                        break

            while l.IS(cls.flag['一层']) :
                click(mu, PCR['地下城:1层'], 0.8, param=[1, True, 1],
                      visi=[PCR['战斗:挑战按钮'], 2000])
                JoinLevelNull.main(mu)
                _visible(mu, PCR['地下城:报酬窗口'], 0.9, timeout=10000)
                click(mu, PCR['地下城:报酬确认'], 0.8, param=[1, True, 1],
                      disa=[mt.SELF, 2000])
                l.set(cls.flag['默认'])

            while l.IS(cls.flag['二层']) :
                click(mu, PCR['地下城:2层'], 0.8, param=[1, True, 1],
                      visi=[PCR['战斗:挑战按钮'], 2000])
                JoinLevelNull.main(mu)
                _visible(mu, PCR['地下城:报酬窗口'], 0.9, timeout=10000)
                click(mu, PCR['地下城:报酬确认'], 0.8, param=[1, True, 1],
                      disa=[mt.SELF, 2000])
                l.set(cls.flag['默认'])

            while l.IS(cls.flag['三层']) :
                click(mu, PCR['地下城:3层'], 0.8, param=[1, True, 1],
                      visi=[PCR['战斗:挑战按钮'], 2000])
                JoinLevelNull.main(mu)
                _visible(mu, PCR['地下城:报酬窗口'], 0.9, timeout=10000)
                click(mu, PCR['地下城:报酬确认'], 0.8, param=[1, True, 1],
                      disa=[mt.SELF, 2000])
                l.set(cls.flag['默认'])

            while l.IS(cls.flag['四层']) :
                click(mu, PCR['地下城:4层'], 0.8, param=[1, True, 1],
                      visi=[PCR['战斗:挑战按钮'], 2000])
                JoinLevelNull.main(mu)
                _visible(mu, PCR['地下城:报酬窗口'], 0.9, timeout=10000)
                click(mu, PCR['地下城:报酬确认'], 0.8, param=[1, True, 1],
                      disa=[mt.SELF, 2000])
                l.set(cls.flag['默认'])

            while l.IS(cls.flag['五层']) :
                # Note 页面：地下城当前第五层 !跳过!
                if cls.ByPassBoss and exist(mu, PCR['地下城:5/5'], 0.9) :
                    l.set(cls.flag['结束'])

            while l.IS(cls.flag['撤退']) :
                # Note 页面：地下城当前第N层 -> 撤退
                #      寻找 {撤退按钮} -> 点击 {撤退} -> 反馈 {撤退窗口}
                #      寻找 {撤退确认按钮} -> 点击 {确认} -> 反馈消失
                click(mu, PCR['地下城:撤退'], 0.8, param=[1, True, 1], visi=[PCR['地下城:撤退窗口'], 2000])
                if exist(mu, PCR['地下城:撤退窗口'], 0.9) :
                    click(mu, PCR['地下城:撤退确认'], 0.8, param=[1, True, 1], disa=[mt.SELF, 0])
                    l.set(cls.flag['结束'])

            # PASS 完成返回
            while l.IS(cls.flag['结束']) :
                logger.info('%s 完成于[%s]' % (Title, l.note()))
                l.set(h, [l.pop])
                return True
        pass

class JoinLevelNull :
    base = 0xFE
    flag = {
        '等待加载' : FlagInit(1, '等待加载', base),
        '配置关卡' : FlagInit(3, '配置关卡', base),
        '配置队伍' : FlagInit(4, '配置队伍', base),
        '等待结束' : FlagInit(5, '等待结束', base),
        '等待结算' : FlagInit(6, '等待结算', base),
    }

    @classmethod
    def main(cls, mu, init=None) :
        Title = '关卡挑战'
        h = l.get()
        if init is None : l.set(cls.flag['配置关卡'], [l.push])
        else : l.set(init, [l.push])

        while l.isBase(cls.base) :
            # PASS L1 关卡面板 画面
            while l.IS(cls.flag['配置关卡']) :
                # Note 寻找 {挑战按钮} -> 点击 {挑战} -> 反馈 {队伍编组面板}
                click(mu, PCR['战斗:挑战按钮'], 0.8, param=[1, True, 1], visi=[PCR['战斗:队伍编组'], 1000])

                # Note 寻找 {队伍编组面板} -> 跳转 L2 队伍配置
                if exist(mu, PCR['战斗:队伍编组'], 0.9) :
                    l.set(cls.flag['配置队伍'])
                    break

                # Note 寻找 {体力不足标志} -> 暂停等待 手动处理
                while True and exist(mu, PCR['战斗:体力不足'], 0.9) :
                    print()
                    logger.error('体力不足 暂停等待手动处理 在显示关卡挑战面板时 输入\回车继续')
                    if input('  ') == '\\' : break

            # PASS L2 队伍配置 画面
            while l.IS(cls.flag['配置队伍']) :
                # Note 寻找 {空队伍标志} -> 点击 {我的队伍} -> 反馈 {呼出此编组按钮}
                #                       -> 点击 [呼出此编组] -> 反馈 {战斗开始按钮}
                if exist(mu, PCR['战斗:队伍编组'], 0.9) and exist(mu, PCR['战斗:空队伍'], 0.9) :
                    click(mu, PCR['战斗:我的队伍'], 0.8, param=[1, True, 1], visi=[PCR['战斗:使用编组'], 0])
                    click(mu, PCR['战斗:使用编组'], 0.8, param=[1, True, 1], visi=[PCR['战斗:战斗开始'], 0])

                # Note 查无 {空队伍标志} -> 寻找 {战斗开始} -> 点击 {战斗开始} -> 反馈消失
                if not exist(mu, PCR['战斗:空队伍'], 0.9) :
                    click(mu, PCR['战斗:战斗开始'], 0.8, param=[1, True, 1], disa=[mt.SELF, 5000])

                # Note 寻找 {载入中} -> 跳转 L3 正在战斗
                if exist(mu, PCR['通用:载入中'], 0.9) : l.set(cls.flag['等待结束'])

            # PASS L3 正在战斗 画面
            while l.IS(cls.flag['等待结束']) :
                # Note 寻找 {自动战斗标志} -> 保持
                if exist(mu, PCR['战斗:自动'], 0.9) or exist(mu, PCR['战斗:时间沙漏'], 0.9) : continue

                # Note 寻找 {战斗胜利标志} -> 跳转 L4 胜利结算
                if exist(mu, PCR['地下城:胜利'], 0.9) or \
                        exist(mu, PCR['战斗:挑战胜利'], 0.9) or \
                        exist(mu, PCR['战斗:玩家等级'], 0.9) or \
                        exist(mu, PCR['战斗:好感度'], 0.9) :
                    l.set(cls.flag['等待结算'])

            # PASS L4 胜利结算 画面
            while l.IS(cls.flag['等待结算']) :
                # Note 寻找 {结算下一步按钮} -> 点击 {下一步} -> 反馈 {自己消失}
                #      寻找 {获得道具/挑战胜利} -> 点击 {获得道具/挑战胜利}
                if retNone == click(mu, PCR['战斗:下一步'], 0.8, param=[1, True, 1], disa=[mt.SELF, 5000]) :
                    click(mu, PCR['战斗:挑战胜利'], 0.8, param=[2, True, 5])
                    click(mu, PCR['战斗:获得道具'], 0.8, param=[2, True, 5])

                # Note 寻找 {限定商店窗口} -> 点击 {取消按钮} -> 反馈消失
                if exist(mu, PCR['战斗:限定商店'], 0.9) :
                    click(mu, PCR['战斗:商店取消'], 0.8, param=[1, True, 1], disa=[mt.SELF, 4000])

                # Note 校验 出现 {载入中} -> 跳转 完成返回
                if exist(mu, PCR['通用:载入中'], 0.9) :
                    l.set(cls.flag['关卡返回'])

            # PASS 完成返回
            while l.IS(cls.flag['关卡返回']) or keyboard.is_pressed('Alt+CTRL') :
                logger.info('%s 完成于[%s]' % (Title, l.note()))
                l.set(h, [l.pop])
                return True

        pass  # while this

class AutoNextLevel :
    base = 0xFE
    flag = {
        '选择关卡' : FlagInit(0, '选择关卡', base),
        '等待加载' : FlagInit(1, '等待加载', base),
        '打开关卡' : FlagInit(2, '打开关卡', base),
        '关卡返回' : FlagInit(7, '关卡返回', base),
        '刷图结束' : FlagInit(8, '刷图结束', base),
    }

    @classmethod
    def main(cls, mu, init=None) :
        Title = '关卡'
        h = l.get()
        if init is None : l.set(cls.flag['选择关卡'], [l.push])
        else : l.set(init, [l.push])

        while l.isBase(cls.base) :
            # PASS 关卡列表 下一关
            while l.IS(cls.flag['选择关卡']) :
                # Note 寻找 {下一关标志} -> 点击 {下一关-偏移} -> 反馈 {关卡挑战按钮}
                click(mu, PCR['战斗:下一关'], 0.9, param=[1, True, 1], visi=[PCR['战斗:挑战按钮'], 500])

                # Note 校验 出现 {关卡挑战按钮} 跳转 -> 关卡挑战
                if exist(mu, PCR['战斗:挑战按钮'], 0.9) :
                    l.set(cls.flag['打开关卡'])
                    break

                # Note 寻找 {下一关备用标志} -> 点击 {备用偏移}
                if not exist(mu, PCR['战斗:下一关'], 0.9) :
                    mat = mu.GetScreen()
                    xy = exist(mu, PCR['战斗:下一关备用'], 0.9, retxy=True)
                    if xy != retNone and type(xy).__name__ != 'bool' :
                        x, y = xy[0] - 50, xy[1] + 60
                        crop = mat[y :y + 90, x :x + 100]
                        if xyFalse != matchtl(crop, PCR['战斗:通关星'], 0.975) :
                            logger.warning('无(未达成一星/两星/三星)未通过的关卡 终止')
                            l.set(cls.flag['刷图结束'])
                        else :
                            click(mu, PCR['战斗:下一关备用'], 0.9, param=[1, True, 1], visi=[PCR['战斗:挑战按钮'], 1000])

                # Note 寻找 {剧情弹窗标志} -> 点击 {取消/关闭} -> 反馈 {自己消失}
                if not exist(mu, PCR['战斗:下一关'], 0.9) and not exist(mu, PCR['战斗:挑战按钮'], 0.9) :
                    click(mu, PCR['战斗:挑战取消'], 0.8, param=[1, True, 1], disa=[mt.SELF, 4000])
                    click(mu, PCR['任务:关闭'], 0.8, param=[1, True, 1], disa=[mt.SELF, 4000])

            # PASS 关卡挑战
            while l.IS(cls.flag['打开关卡']) :
                # Note 开始挑战 等待结束 -> 关卡返回
                JoinLevelNull.main(mu)
                l.set(cls.flag['关卡返回'])

            # PASS 关卡返回
            while l.IS(cls.flag['关卡返回']) :
                # Note 寻找 {普通难度标志} -> 关卡列表 下一关
                if exist(mu, PCR['主线:普通'], 0.9) : l.set(cls.flag['选择关卡'])

            # PASS 终止
            while l.IS(cls.flag['刷图结束']) or keyboard.is_pressed('Alt+CTRL') :
                logger.info('%s 完成于[%s]' % (Title, l.note()))
                l.set(h, [l.pop])
                return True

        pass  # while this

class AutoLogin :
    base = 0xFF
    flag = {
        'PCR'   : FlagInit(1, 'PCR', base),
        '运行'    : FlagInit(2, '主程序', base),
        '点击登录'  : FlagInit(3, '登录界面', base),
        '每日签到'  : FlagInit(4, '每日盖章', base),
        '特色活动'  : FlagInit(5, '特色活动', base),
        '通告预告'  : FlagInit(6, '通知预告', base),
        '活动'    : FlagInit(7, '活动', base),
        '通告'    : FlagInit(8, '通告', base),
        '兰德索尔杯' : FlagInit(9, '通告', base),
        '我的冒险'  : FlagInit(10, '主页', base),
        '冒险'    : FlagInit(11, '冒险', base),
    }

    @classmethod
    def Login(cls, mu, init=None) :
        Title = '登录'
        h = l.get()
        if init is None : l.set(cls.flag['运行'])
        else : l.set(init)

        while l.isBase(cls.base) :
            # PASS 游戏主程序载入
            while l.IS(cls.flag['运行']) :
                # Note 寻找 {点击屏幕 登陆游戏} -> 点击登录界面
                if exist(mu, PCR['登录:点击屏幕'], 0.9) : l.set(cls.flag['点击登录'], [l.push])

            # PASS 点击登录界面
            while l.IS(cls.flag['点击登录']) :
                # Note 寻找 {点击屏幕 登陆游戏} -> 点击 {点击屏幕} -> 反馈 {自己消失}
                click(mu, PCR['登录:点击屏幕'], 0.8, param=[1, True, 1], disa=[mt.SELF, 5000])

                # Note 寻找 {签到跳过按钮} 跳转 -> 每日签到界面
                if exist(mu, PCR['登录:跳过'], 0.9) :
                    l.set(cls.flag['每日签到'])
                    break

                # Note 寻找 {通知窗口} 跳转 -> 主界面通知窗口
                if exist(mu, PCR['通告:通知活动'], 0.9) :
                    l.set(cls.flag['通告预告'])
                    break

                if exist(mu, PCR['兰德索尔杯:选择角色'], 0.9) :
                    l.set(cls.flag['兰德索尔杯'])
                    break

            # PASS 当日首次登录
            while l.IS(cls.flag['每日签到']) :
                # Note 寻找 {签到跳过按钮} -> 点击 {跳过按钮} -> 反馈 {自己消失}
                click(mu, PCR['登录:跳过'], 0.8, param=[1, True, 1], disa=[mt.SELF, 5000])

                # Note 寻找 {通知窗口} 跳转 -> 主界面通知窗口
                if exist(mu, PCR['通告:通知活动'], 0.9) :
                    l.set(cls.flag['通告预告'])
                    break

                if exist(mu, PCR['兰德索尔杯:选择角色'], 0.9) :
                    l.set(cls.flag['兰德索尔杯'])
                    break

            # PASS 兰德索尔杯
            while l.IS(cls.flag['兰德索尔杯']) :
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
                        l.set(cls.flag['通告预告'])
                        break

                # Note 寻找 {通知窗口} 跳转 -> 主界面通知窗口
                if exist(mu, PCR['通告:通知活动'], 0.9) :
                    l.set(cls.flag['通告预告'])
                    break

            # PASS 主界面通知窗口
            while l.IS(cls.flag['通告预告']) :
                # Note 寻找 {通知/活动标志} -> 点击 {关闭按钮} -> 反馈 {自己消失}
                if exist(mu, PCR['通告:通知活动'], 0.9) :
                    click(mu, PCR['通告:关闭按钮'], 0.8, param=[1, True, 1], disa=[mt.SELF, 1000])
                    # Note 寻找 {导航主页按钮} 跳转 -> 登陆完成
                    while not exist(mu, PCR['导航:主页'], 0.9) : pass
                    l.set(cls.flag['我的冒险'])

            # PASS 登陆完成
            while l.IS(cls.flag['我的冒险']) or keyboard.is_pressed('Alt+CTRL') :
                logger.info('%s 完成于[%s]' % (Title, l.note()))
                l.set(h, [l.pop])
                return True

        pass  # while this

logger.warning('进入主循环,按住[Alt+MENU]可暂停，按住[Alt+WIN]继续\n')

GetMuHandler()
MEMU = mudevice("127.0.0.1:21503", "VM", "/dev/input/event6")
MEMU.connect()

l = FlagCtrl(flag=AutoLogin.flag['PCR'], pause=False)
l.set(AutoLogin.flag['运行'], [l.root])

def main() :
    # AutoLogin.main(MEMU)
    # AutoNextLevel.main(MEMU)
    AutoDungeon.main(MEMU)
    # AutoExplore.main(MEMU)
    # AutoStore.main(MEMU, cls.flag['通常'] ,Ignore=True)
    exit()
    pass

if __name__ == '__main__' :
    while True :
        if keyboard.is_pressed('Alt+MENU') :
            if not l.pause : print('\033[1;31;40m'"[暂停]\n")
            l.pause = True
        if keyboard.is_pressed('Alt+WIN') :
            if l.pause : print('\033[1;32;40m'"[继续]\n")
            l.pause = False
        if not l.pause : main()
