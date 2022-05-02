from _public import cal, definetl as tl, fbSelf, mo, roiFull

# root = ".\\PCR1280x720\\"
#
# PCR = dict()
#
# PCR['登录:点击屏幕'] = tl(root, "#00-0.png", "登录:点击屏幕", roiFull, fbSelf, [tl.RGBA])
# PCR['登录:主菜单'] = tl(root, "#00-1.png", "登录:主菜单按钮", roiFull, fbSelf, [tl.RGB])
# PCR['登录:适龄'] = tl(root, "#00-2.png", "登录:适龄12+", roiFull, fbSelf, [tl.RGB])
# PCR['登录:签到'] = tl(root, "#00-3.png", "登录:每日签到", roiFull, fbSelf, [tl.RGB])
#
# PCR['账号:切换'] = tl(root, "#01-0.png", "账号:切换账号", roiFull, fbSelf, [tl.RGB])
# PCR['账号:上次'] = tl(root, "#01-1.png", "账号:上次登录", roiFull, fbSelf, [tl.RGB])
# PCR['账号:登录'] = tl(root, "#01-2.png", "账号:登录", roiFull, fbSelf, [tl.RGB])
# PCR['账号:列表'] = tl(root, "#01-3.png", "账号:账号列表", roiFull, fbSelf, [tl.RGB])
#
# PCR['登录:活动结束'] = tl(root, "#02-0.png", "登录:活动结束预告", roiFull, fbSelf, [tl.RGB])
# PCR['登录:通知窗口'] = tl(root, "#02-1.png", "登录:通知窗口", roiFull, fbSelf, [tl.RGB])
#
# PCR['账号:返回标题'] = tl(root, "#05-0.png", "账号:返回标题页面", roiFull, fbSelf, [tl.RGB])
# PCR['账号:确认注销'] = tl(root, "#05-1.png", "账号:确认注销窗口", roiFull, fbSelf, [tl.RGB])
#
# PCR['导航:我的主页'] = [
#     tl(root, "#10-1.png", "导航:我的主页", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#10-1C.png", "导航:我的主页", roiFull, fbSelf, [tl.RGB])]
# PCR['导航:角色'] = [
#     tl(root, "#10-2.png", "导航:角色", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#10-2C.png", "导航:角色", roiFull, fbSelf, [tl.RGB])]
# PCR['导航:剧情'] = [
#     tl(root, "#10-3.png", "导航:剧情", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#10-3C.png", "导航:剧情", roiFull, fbSelf, [tl.RGB])]
# PCR['导航:冒险'] = [
#     tl(root, "#10-4.png", "导航:冒险", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#10-4C.png", "导航:冒险", roiFull, fbSelf, [tl.RGB])]
# PCR['导航:工会之家'] = [
#     tl(root, "#10-5.png", "导航:工会之家", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#10-5C.png", "导航:工会之家", roiFull, fbSelf, [tl.RGB])]
# PCR['导航:扭蛋'] = [
#     tl(root, "#10-6.png", "导航:扭蛋", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#10-6C.png", "导航:扭蛋", roiFull, fbSelf, [tl.RGB])]
# PCR['导航:主菜单'] = [
#     tl(root, "#10-7.png", "导航:主菜单", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#10-7C.png", "导航:主菜单", roiFull, fbSelf, [tl.RGB])]
#
# PCR['主页:商店'] = tl(root, "#11-0.png", "主页:商店", roiFull, fbSelf, [tl.RGB])
# PCR['主页:行会'] = tl(root, "#12-0.png", "主页:行会", roiFull, fbSelf, [tl.RGB])
# PCR['主页:任务'] = tl(root, "#13-0.png", "主页:任务", roiFull, fbSelf, [tl.RGB])
# PCR['主页:礼物'] = tl(root, "#15-0.png", "主页:礼物", roiFull, fbSelf, [tl.RGB])
#
# PCR['商店:选框'] = tl(root, "#11-1-0-0.png", "商店:选框", roiFull, fbSelf, [tl.RGB])
# PCR['商店:选框半个'] = tl(root, "#11-1-0-1.png", "商店:半个选框", roiFull, fbSelf, [tl.RGB])
# PCR['商店:立即更新'] = tl(root, "#11-1-0-2.png", "商店:立即更新", roiFull, fbSelf, [tl.RGB])
# PCR['商店:通常'] = tl(root, "#11-1-1-1.png", "商店:通常", roiFull, fbSelf, [tl.RGB])
# PCR['商店:地下城'] = tl(root, "#11-1-1-2.png", "商店:地下城", roiFull, fbSelf, [tl.RGB])
# PCR['商店:JJC'] = tl(root, "#11-1-1-3.png", "商店:JJC", roiFull, fbSelf, [tl.RGB])
# PCR['商店:PJJC'] = tl(root, "#11-1-1-4.png", "商店:PJJC", roiFull, fbSelf, [tl.RGB])
# PCR['商店:行会'] = tl(root, "#11-1-1-5.png", "商店:行会", roiFull, fbSelf, [tl.RGB])
# PCR['商店:大师'] = tl(root, "#11-1-1-6.png", "商店:大师", roiFull, fbSelf, [tl.RGB])
#
# PCR['任务:全部收取'] = tl(root, "#13-1.png", "任务:全部收取", roiFull, fbSelf, [tl.RGB])
#
# PCR['礼物:窗口'] = tl(root, "#15-1.png", "礼物:窗口", roiFull, fbSelf, [tl.RGB])
# PCR['礼物:全部收取'] = tl(root, "#15-2.png", "礼物:全部收取", roiFull, fbSelf, [tl.RGB])
#
# PCR['剧情:New'] = tl(root, "#30-0.png", "剧情:新内容", roiFull, fbSelf, [tl.RGB])
# PCR['剧情:主线'] = tl(root, "#30-1.png", "剧情:主线", roiFull, fbSelf, [tl.RGB])
# PCR['剧情:角色'] = tl(root, "#30-2.png", "剧情:角色", roiFull, fbSelf, [tl.RGB])
# PCR['剧情:公会'] = tl(root, "#30-3.png", "剧情:公会", roiFull, fbSelf, [tl.RGB])
# PCR['剧情:特别'] = tl(root, "#30-4.png", "剧情:特别", roiFull, fbSelf, [tl.RGB])
#
# PCR['冒险:主线'] = tl(root, "#41-0.png", "冒险:主线", roiFull, fbSelf, [tl.RGB])
# PCR['主线:普通'] = [
#     tl(root, "#41-0-1.png", "主线:高难", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#41-0-1-1.png", "主线:高难", roiFull, fbSelf, [tl.RGB])]
# PCR['主线:困难'] = [
#     tl(root, "#41-0-2.png", "主线:高难", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#41-0-2-1.png", "主线:高难", roiFull, fbSelf, [tl.RGB])]
# PCR['主线:高难'] = [
#     tl(root, "#41-0-3.png", "主线:高难", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#41-0-3-1.png", "主线:高难", roiFull, fbSelf, [tl.RGB])]
#
# PCR['主线:扫荡'] = tl(root, "#41-0-4.png", "主线:扫荡", roiFull, fbSelf, [tl.RGBA])
# PCR['扫荡:关卡一栏'] = tl(root, "#41-0-4-0.png", "扫荡:关卡一栏", roiFull, fbSelf, [tl.RGB])
# PCR['扫荡:一键扫荡'] = tl(root, "#41-0-4-1.png", "扫荡:一键扫荡", roiFull, fbSelf, [tl.RGB])
#
# PCR['冒险:探索'] = tl(root, "#42-0.png", "冒险:探索", roiFull, fbSelf, [tl.RGB])
# PCR['探索:经验关卡'] = tl(root, "#42-0-1.png", "探索:经验关卡", roiFull, fbSelf, [tl.RGB])
# PCR['探索:玛那关卡'] = tl(root, "#42-0-2.png", "探索:玛那关卡", roiFull, fbSelf, [tl.RGB])
# PCR['探索:关卡'] = tl(root, "#42-0-3.png", "探索:关卡", roiFull, fbSelf, [tl.RGB])
# PCR['探索:前往经验关卡'] = tl(root, "#42-0-4.png", "探索:前往经验关卡", roiFull, fbSelf, [tl.RGB])
# PCR['探索:前往探索首页'] = tl(root, "#42-0-5.png", "探索:前往探索首页", roiFull, fbSelf, [tl.RGB])
#
# PCR['冒险:地下城'] = tl(root, "#43-0.png", "冒险:地下城", roiFull, fbSelf, [tl.RGB])
# PCR['冒险:极难3'] = tl(root, "#43_0_1.png", "冒险:极难3", roiFull, fbSelf, [tl.RGB])
# PCR['地下城:选择'] = tl(root, "#43-0-0S.png", "地下城:选择", roiFull, fbSelf, [tl.RGB])
# PCR['地下城:层数'] = [
#     tl(root, "#43-0-1F.png", "地下城:1F", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "#43-0-2F.png", "地下城:2F", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "#43-0-3F.png", "地下城:3F", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "#43-0-4F.png", "地下城:4F", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "#43-0-5F.png", "地下城:5F", roiFull, fbSelf, [tl.RGBA])]
# PCR['地下城:过场'] = tl(root, "#43-0-6G.png", "地下城:过场", roiFull, fbSelf, [tl.RGB])
# PCR['地下城:撤退'] = tl(root, "#43-0-7R.png", "地下城:撤退", roiFull, fbSelf, [tl.RGB])
#
# PCR['冒险:调查'] = tl(root, "#44-0.png", "冒险:调查", roiFull, fbSelf, [tl.RGB])
# PCR['调查:圣迹调查'] = tl(root, "#44-0-1.png", "调查:圣迹调查", roiFull, fbSelf, [tl.RGB])
# PCR['调查:神殿调查'] = tl(root, "#44-0-2.png", "调查:神殿调查", roiFull, fbSelf, [tl.RGB])
#
# PCR['冒险:团队战'] = tl(root, "#45-0.png", "冒险:团队战", roiFull, fbSelf, [tl.RGB])
#
# PCR['冒险:JJC'] = tl(root, "#46-1.png", "冒险:战斗竞技场", roiFull, fbSelf, [tl.RGB])
# PCR['冒险:PJJC'] = tl(root, "#46-2.png", "冒险:公主竞技场", roiFull, fbSelf, [tl.RGB])
# PCR['竞技场:列表更新'] = tl(root, "#46-0-0.png", "竞技场:列表更新", roiFull, fbSelf, [tl.RGB])
# PCR['竞技场:剩余编组'] = tl(root, "#46-0-1.png", "竞技场:剩余编组时间", roiFull, fbSelf, [tl.RGB])
# PCR['竞技场:收取'] = tl(root, "#46-0-2.png", "竞技场:收取", roiFull, fbSelf, [tl.RGB])
# PCR['竞技场:跳过'] = tl(root, "#46-0-3.png", "竞技场:跳过", roiFull, fbSelf, [tl.RGB])
# PCR['竞技场:下一步"'] = tl(root, "#46-0-4.png", "竞技场:下一步", roiFull, fbSelf, [tl.RGB])
#
# PCR['冒险:活动'] = tl(root, "#48-0.png", "冒险:剧情活动", roiFull, fbSelf, [tl.RGB])
# PCR['冒险:外传'] = tl(root, "#48-0-1.png", "冒险:外传", roiFull, fbSelf, [tl.RGB])
# PCR['活动:困难1-1'] = tl(root, "#48-0-1-1.png", "剧情活动:困难1-1", roiFull, fbSelf, [tl.RGBA])
# PCR['活动:高难BOSS'] = tl(root, "#48-0-1-2.png", "剧情活动:高难BOSS", roiFull, fbSelf, [tl.RGB])
#
# PCR['活动:关卡'] = tl(root, "#48-1.png", "活动:活动关卡", roiFull, fbSelf, [tl.RGB])
#
# PCR['工会之家:全部收取'] = tl(root, "#50-0-1.png", "工会之家:全部收取", roiFull, fbSelf, [tl.RGB])
#
# PCR['通用:确认'] = [
#     tl(root, "#98-0-1.png", "通用:确认1", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#98-0-2.png", "通用:确认2", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#98-0-3.png", "通用:确认3", roiFull, fbSelf, [tl.RGB])
# ]
#
# PCR['通用:关闭'] = [
#     tl(root, "#98-1-1.png", "通用:关闭1", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#98-1-2.png", "通用:关闭2", roiFull, fbSelf, [tl.RGB]),
#     tl(root, "#98-1-3.png", "通用:关闭3", roiFull, fbSelf, [tl.RGB]),
# ]
#
# PCR['通用:取消'] = tl(root, "#98-2-1.png", "通用:取消1", roiFull, fbSelf, [tl.RGB])
#
# PCR['通用:载入中'] = tl(root, "#99-1-0.png", "通用:载入中", roiFull, fbSelf, [tl.RGB])
# PCR['通用:自动'] = tl(root, "#99-1-1.png", "通用:自动", roiFull, fbSelf, [tl.RGB])
# PCR['通用:返回'] = tl(root, "#99-1-2.png", "通用:返回", roiFull, fbSelf, [tl.RGB])
# PCR['通用:对话'] = tl(root, "#99-1-3.png", "通用:对话", roiFull, fbSelf, [tl.RGB])
#
# PCR['通用:队伍空位'] = tl(root, "#99-2-2.png", "通用:队伍空位", roiFull, fbSelf, [tl.RGB])
# PCR['通用:我的队伍'] = tl(root, "#99-2-0.png", "通用:我的队伍", roiFull, fbSelf, [tl.RGB])
# PCR['队伍:呼出编组'] = tl(root, "#99-2-1.png", "我的队伍:呼出编组", roiFull, fbSelf, [tl.RGB])
#
# PCR['扫荡:加'] = tl(root, "#99-3-1.png", "扫荡:加", roiFull, fbSelf, [tl.RGB])
# PCR['扫荡:使用'] = tl(root, "#99-3-2.png", "扫荡:使用", roiFull, fbSelf, [tl.RGB])
# PCR['扫荡:击破'] = tl(root, "#99-3-3.png", "扫荡:击破", roiFull, fbSelf, [tl.RGB])
# PCR['扫荡:跳过'] = tl(root, "#99-3-4.png", "扫荡:跳过完毕", roiFull, fbSelf, [tl.RGB])
#
# PCR['战斗:备用头'] = tl(root, "#99-4-0-1.png", "战斗:下一关", roiFull, cal(mo.SELF, -50, 40, 100, 75), [tl.RGB])
# PCR['战斗:下一关'] = [
#     tl(root, "#99-4-0.png", "战斗:下一关", roiFull, cal(mo.SELF, -60, 100, 120, 80), [tl.RGBA]),
#     tl(root, "#99-4-0-1.png", "战斗:下一关", roiFull, cal(mo.SELF, -50, 70, 120, 80), [tl.RGBA])
# ]
#
# PCR['战斗:挑战'] = tl(root, "#99-4-1.png", "战斗:挑战", roiFull, fbSelf, [tl.RGB])
# PCR['战斗:开始'] = tl(root, "#99-4-2.png", "战斗:战斗开始", roiFull, fbSelf, [tl.RGB])
# PCR['战斗:胜利'] = tl(root, "#99-4-3.png", "战斗:胜利", roiFull, fbSelf, [tl.RGB])
# PCR['战斗:下一步'] = tl(root, "#99-4-4.png", "战斗:下一步", roiFull, fbSelf, [tl.RGB])
# PCR['战斗:限定商店'] = tl(root, "#99-4-5.png", "战斗:限定商店出现", roiFull, fbSelf, [tl.RGB])
#
# print()

# PCR = dict()
#
# # ----------------------------------------------------------------
# #   登录 流程
#
# PCR['登录01点击屏幕'] = [
#     tl(root, "00登录01点击屏幕.png", "00登录01点击屏幕", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "00登录01开始游戏.png", "00登录01开始游戏", roiFull, fbSelf, [tl.RGBA])]
#
# PCR['登录02跳过'] = tl(root, "00登录02跳过按钮.png", "00登录02跳过按钮", roiFull, fbSelf, [tl.RGBA])
#
# PCR['帐号02切换'] = tl(root, "00登录02切换帐号.png", "00登录02切换帐号", roiFull, fbSelf, [tl.RGBA])
# PCR['账号01列表'] = tl(root, "01账号01列表按钮.png", "01账号01列表按钮", roiFull, fbSelf, [tl.RGBA])
# PCR['账号01上次'] = tl(root, "01账号01上次登录.png", "01账号01上次登录", roiFull, fbSelf, [tl.RGBA])
# PCR['账号01登录'] = tl(root, "01账号01登录按钮.png", "01账号01登录按钮", roiFull, fbSelf, [tl.RGBA])
#
# PCR['账号04取消'] = tl(root, "01账号04取消按钮.png", "01账号04取消按钮", roiFull, fbSelf, [tl.RGBA])
# PCR['账号04确认'] = tl(root, "01账号04确认按钮.png", "01账号04确认按钮", roiFull, fbSelf, [tl.RGBA])
#
# PCR['兰德索尔杯:选择角色'] = tl(root, "02活动.兰德索尔杯.选择角色.png", "02活动.兰德索尔杯.选择角色", roiFull, fbSelf, [tl.RGBA])
# PCR['兰德索尔杯:旗帜'] = [
#     tl(root, "02活动.兰德索尔杯.旗1.png", "02活动.兰德索尔杯.旗1", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "02活动.兰德索尔杯.旗2.png", "02活动.兰德索尔杯.旗2", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "02活动.兰德索尔杯.旗3.png", "02活动.兰德索尔杯.旗3", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "02活动.兰德索尔杯.旗4.png", "02活动.兰德索尔杯.旗4", roiFull, fbSelf, [tl.RGBA])]
# PCR['兰德索尔杯:开始'] = tl(root, "02活动.兰德索尔杯.竞赛开始按钮.png", "02活动.兰德索尔杯.竞赛开始按钮", roiFull, fbSelf, [tl.RGBA])
# PCR['兰德索尔杯:跳过'] = tl(root, "02活动.兰德索尔杯.跳过按钮.png", "02活动.兰德索尔杯.跳过按钮", roiFull, fbSelf, [tl.RGBA])
# PCR['兰德索尔杯:结果'] = tl(root, "02活动.兰德索尔杯.结果.png", "02活动.兰德索尔杯.结果", roiFull, fbSelf, [tl.RGBA])
#
# PCR['通告01活动结束'] = tl(root, "03通告01活动结束通告页面.png", "03通告01活动结束通告页面", roiFull, fbSelf, [tl.RGBA])
# PCR['通告:通知页面'] = tl(root, "03通告02通知页面.png", "03通告02通知页面", roiFull, fbSelf, [tl.RGBA])
# PCR['通告01取消按钮'] = [
#     tl(root, "03通告01取消按钮.png", "03通告01取消按钮", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "03通告02取消按钮.png", "03通告02取消按钮", roiFull, fbSelf, [tl.RGBA])]
#
# # ----------------------------------------------------------------
# #   游戏 路由 流程
#
# PCR['导航:主页'] = [
#     tl(root, "04导航01主页.png", "04导航01主页", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "04导航01主页选定.png", "04导航01主页选定", roiFull, fbSelf, [tl.RGBA])]
# PCR['导航:角色'] = [
#     tl(root, "04导航02角色.png", "04导航02角色", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "04导航02角色选定.png", "04导航02角色选定", roiFull, fbSelf, [tl.RGBA])]
# PCR['导航:剧情'] = [
#     tl(root, "04导航03剧情.png", "04导航03剧情", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "04导航03剧情选定.png", "04导航03剧情选定", roiFull, fbSelf, [tl.RGBA])]
# PCR['导航:冒险'] = [
#     tl(root, "04导航04冒险.png", "04导航04冒险", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "04导航04冒险选定.png", "04导航04冒险选定", roiFull, fbSelf, [tl.RGBA])]
# PCR['导航:之家'] = [
#     tl(root, "04导航05之家.png", "04导航05之家", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "04导航05之家选定.png", "04导航05之家选定", roiFull, fbSelf, [tl.RGBA])]
# PCR['导航:抽卡'] = [
#     tl(root, "04导航06抽卡.png", "04导航06抽卡", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "04导航06抽卡选中.png", "04导航06抽卡选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['导航:主菜单'] = [
#     tl(root, "04导航07主菜单.png", "04导航07主菜单", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "04导航07主菜单选中.png", "04导航07主菜单选中", roiFull, fbSelf, [tl.RGBA])]
#
# PCR['剧情:主线'] = tl(root, "04剧情01主线.png", "04剧情01主线", roiFull, fbSelf, [tl.RGBA])
# PCR['剧情:角色'] = tl(root, "04剧情02角色.png", "04剧情02角色", roiFull, fbSelf, [tl.RGBA])
# PCR['剧情:公会'] = tl(root, "04剧情03公会.png", "04剧情03公会", roiFull, fbSelf, [tl.RGBA])
# PCR['剧情:特别'] = tl(root, "04剧情04特别.png", "04剧情04特别", roiFull, fbSelf, [tl.RGBA])
# PCR['剧情:新内容'] = [
#     tl(root, "04剧情05新内容.png", "04剧情05新内容", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "04剧情06新内容.png", "04剧情06新内容", roiFull, fbSelf, [tl.RGBA])]
#
# PCR['公会之家:全部收取'] = tl(root, "04公会之家01全部收取按钮.png", "04公会之家01全部收取按钮", roiFull, fbSelf, [tl.RGBA])
#
# PCR['抽卡:每日标志'] = tl(root, "04抽卡01每日刷新.png", "04抽卡01每日刷新", roiFull, fbSelf, [tl.RGBA])
# PCR['抽卡:每日刷新'] = tl(root, "04抽卡02每日刷新.png", "04抽卡02每日刷新", roiFull, fbSelf, [tl.RGBA])
# PCR['抽卡:每日十连'] = tl(root, "04抽卡03每日十连.png", "04抽卡03每日十连", roiFull, fbSelf, [tl.RGBA])
#
# PCR['主页:商店'] = tl(root, "04按钮01商店.png", "04按钮01商店", roiFull, fbSelf, [tl.RGBA])
# PCR['主页:行会'] = tl(root, "04按钮02行会.png", "04按钮02行会", roiFull, fbSelf, [tl.RGBA])
# PCR['主页:通知'] = tl(root, "04按钮03通知.png", "04按钮03通知", roiFull, fbSelf, [tl.RGBA])
# PCR['主页:任务'] = tl(root, "04按钮04任务.png", "04按钮04任务", roiFull, fbSelf, [tl.RGBA])
# PCR['主页:礼物'] = tl(root, "04按钮05礼物.png", "04按钮05礼物", roiFull, fbSelf, [tl.RGBA])
#
# # ----------------------------------------------------------------
# #   冒险 流程
#
# PCR['冒险:主线'] = tl(root, "04冒险01主线.png", "04冒险01主线", roiFull, fbSelf, [tl.RGBA])
# PCR['冒险:探索'] = tl(root, "04冒险02探索.png", "04冒险02探索", roiFull, fbSelf, [tl.RGBA])
# PCR['冒险:地下城'] = tl(root, "04冒险03地下城.png", "04冒险03地下城", roiFull, fbSelf, [tl.RGBA])
# PCR['冒险:4调查'] = tl(root, "04冒险04调查.png", "04冒险04调查", roiFull, fbSelf, [tl.RGBA])
# PCR['冒险:团队战'] = tl(root, "04冒险05团队战.png", "04冒险05团队战", roiFull, fbSelf, [tl.RGBA])
# PCR['冒险:战斗竞技场'] = tl(root, "04冒险06战斗竞技场.png", "04冒险06战斗竞技场", roiFull, fbSelf, [tl.RGBA])
# PCR['冒险:公主竞技场'] = tl(root, "04冒险06公主竞技场.png", "04冒险06公主竞技场", roiFull, fbSelf, [tl.RGBA])
#
# PCR['冒险:露娜'] = tl(root, "04冒险07露娜之塔.png", "04冒险07露娜之塔", roiFull, fbSelf, [tl.RGBA])
# PCR['冒险:复刻'] = tl(root, "04冒险08复刻.png", "04冒险08复刻", roiFull, fbSelf, [tl.RGBA])
# PCR['冒险:活动'] = tl(root, "04冒险08活动.png", "04冒险08活动", roiFull, fbSelf, [tl.RGBA])
# PCR['冒险:外传'] = tl(root, "04冒险09外传.png", "04冒险09外传", roiFull, fbSelf, [tl.RGBA])
#
# # ----------------------------------------------------------------
# #   商店 任务 礼物 流程
#
# PCR['礼物:礼物箱'] = tl(root, "05礼物01礼物箱窗口.png", "05礼物01礼物箱窗口", roiFull, fbSelf, [tl.RGBA])
# PCR['礼物:全部收取'] = tl(root, "05礼物01全部收取按钮.png", "05礼物01全部收取按钮", roiFull, fbSelf, [tl.RGBA])
#
# PCR['任务:全部收取'] = tl(root, "05任务01全部收取.png", "05任务01全部收取", roiFull, fbSelf, [tl.RGBA])
# PCR['任务:关闭'] = tl(root, "05任务02关闭.png", "05任务02关闭", roiFull, fbSelf, [tl.RGBA])
#
# PCR['商店:通常'] = [
#     tl(root, "05商店01通常.png", "05商店01通常", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "05商店01通常选中.png", "05商店01通常选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['商店:地下城'] = [
#     tl(root, "05商店02地下城.png", "05商店02地下城", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "05商店02地下城选中.png", "05商店02地下城选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['商店:竞技场'] = [
#     tl(root, "05商店03竞技场.png", "05商店03竞技场", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "05商店03竞技场选中.png", "05商店03竞技场选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['商店:公主'] = [
#     tl(root, "05商店04公主竞技场.png", "05商店04公主竞技场", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "05商店04公主竞技场选中.png", "05商店04公主竞技场选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['商店:行会'] = [
#     tl(root, "05商店05行会.png", "05商店05行会", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "05商店05行会选中.png", "05商店05行会选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['商店:大师'] = [
#     tl(root, "05商店06大师.png", "05商店06大师", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "05商店06大师选中.png", "05商店06大师选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['商店:秘石'] = [
#     tl(root, "05商店07秘石.png", "05商店07秘石", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "05商店07秘石选中.png", "05商店07秘石选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['商店:限定'] = [
#     tl(root, "05商店08限定.png", "05商店08限定", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "05商店08限定选中.png", "05商店08限定选中", roiFull, fbSelf, [tl.RGBA])]
#
# PCR['商店:选框'] = tl(root, "05商店10批量选框.png", "05商店10批量选框", roiFull, fbSelf, [tl.RGBA])
# PCR['商店:选框半'] = tl(root, "05商店10批量选框半.png", "05商店10批量选框半", roiFull, fbSelf, [tl.RGBA])
# PCR['商店:十万更新'] = tl(root, "05商店11十万立刻更新.png", "05商店11十万立刻更新", roiFull, fbSelf, [tl.RGBA])
# PCR['商店:立刻更新'] = tl(root, "05商店12立刻更新.png", "05商店12立刻更新", roiFull, fbSelf, [tl.RGBA])
# PCR['商店:批量购入'] = tl(root, "05商店12批量购入.png", "05商店12批量购入", roiFull, fbSelf, [tl.RGBA])
# PCR['商店:超级经验'] = tl(root, "05商店20超级经验药剂.png", "05商店20超级经验药剂", roiFull, fbSelf, [tl.RGBA])
#
# # ----------------------------------------------------------------
# #   战斗 流程
#
# PCR['战斗:下一关'] = [
#     tl(root, "11战斗01下一关.png", "11战斗01下一关", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "11战斗01下一关箭头.png", "11战斗01下一关箭头", roiFull, fbSelf, [tl.RGBA])]
#
# PCR['战斗:一星'] = tl(root, "11战斗01一心.png", "11战斗01一心", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:二星'] = tl(root, "11战斗01二心.png", "11战斗01二心", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:三星'] = tl(root, "11战斗01三心.png", "11战斗01三心", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:满星'] = tl(root, "11战斗01满心.png", "11战斗01满心", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:星'] = [PCR['战斗:一星'], PCR['战斗:二星'], PCR['战斗:三星'], PCR['战斗:满星']]
#
# PCR['战斗:次数用完'] = tl(root, "11战斗01次数用完.png", "11战斗01次数用完", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:上一关卡'] = tl(root, "11战斗01上一关卡.png", "11战斗01上一关卡", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:下一关卡'] = tl(root, "11战斗01下一关卡.png", "11战斗01下一关卡", roiFull, fbSelf, [tl.RGBA])
#
# PCR['扫荡:批量'] = tl(root, "10扫荡01批量.png", "10扫荡01批量", roiFull, fbSelf, [tl.RGBA])
# PCR['扫荡:一键扫荡'] = tl(root, "10扫荡02一键扫荡按钮.png", "10扫荡02一键扫荡按钮", roiFull, fbSelf, [tl.RGBA])
# PCR['扫荡:加'] = tl(root, "10扫荡03加号.png", "10扫荡03加号", roiFull, fbSelf, [tl.RGBA])
# PCR['扫荡:确认'] = tl(root, "10扫荡05确认.png", "10扫荡05确认", roiFull, fbSelf, [tl.RGBA])
# PCR['扫荡:合计获得'] = tl(root, "10扫荡04合计获得报酬.png", "10扫荡04合计获得报酬", roiFull, fbSelf, [tl.RGBA])
# PCR['扫荡:跳过完毕'] = tl(root, "10扫荡05跳过完毕.png", "10扫荡05跳过完毕", roiFull, fbSelf, [tl.RGBA])
#
# PCR['战斗:挑战按钮'] = tl(root, "11战斗01挑战按钮.png", "11战斗01挑战按钮", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:挑战取消'] = tl(root, "11战斗01取消按钮.png", "11战斗01取消按钮", roiFull, fbSelf, [tl.RGBA])
#
# PCR['战斗:空队伍'] = tl(root, "11战斗02空队伍.png", "11战斗02空队伍", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:我的队伍'] = tl(root, "11战斗02我的队伍.png", "11战斗02我的队伍", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:队伍一览'] = tl(root, "11战斗02队伍一览.png", "11战斗02队伍一览", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:使用编组'] = tl(root, "11战斗02使用编组.png", "11战斗02使用编组", roiFull, fbSelf, [tl.RGBA])
#
# PCR['战斗:时间沙漏'] = tl(root, "11战斗03沙漏.png", "11战斗03沙漏", roiFull, fbSelf, [tl.RGBA])
# PCR['对话:名片'] = tl(root, "12对话01.png", "12对话01", roiFull, fbSelf, [tl.RGBA])
# PCR['对话:箭头'] = tl(root, "12对话02.png", "12对话02", roiFull, fbSelf, [tl.RGBA])
#
# PCR['地下城:胜利'] = tl(root, "24地下城02胜利.png", "24地下城02胜利", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:挑战胜利'] = tl(root, "11战斗03挑战胜利.png", "11战斗03挑战胜利", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:玩家等级'] = tl(root, "11战斗03玩家等级.png", "11战斗03玩家等级", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:好感度'] = tl(root, "11战斗03好感度.png", "11战斗03好感度", roiFull, fbSelf, [tl.RGBA])
#
# PCR['战斗:限定商店'] = tl(root, "11战斗03限定商店.png", "11战斗03限定商店", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:商店取消'] = tl(root, "11战斗03取消.png", "11战斗03取消", roiFull, fbSelf, [tl.RGBA])
#
# PCR['战斗:自动'] = tl(root, "11战斗03自动.png", "11战斗03自动", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:一倍'] = tl(root, "11战斗03一倍.png", "11战斗03一倍", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:二倍'] = tl(root, "11战斗03二倍.png", "11战斗03二倍", roiFull, fbSelf, [tl.RGBA])
# PCR['战斗:三倍'] = tl(root, "11战斗03三倍.png", "11战斗03三倍", roiFull, fbSelf, [tl.RGBA])
#
# # ----------------------------------------------------------------
# #   地下城 流程
#
# PCR['地下城:剩余次数'] = tl(root, "24地下城01剩余挑战次数.png", "24地下城01剩余挑战次数", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:次数用完'] = tl(root, "24地下城01零次.png", "24地下城01零次", roiFull, fbSelf, [tl.RGBA])
#
# PCR['地下城:EX3'] = tl(root, "24地下城EX3.png", "24地下城EX3", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:确认地域'] = tl(root, "24地下城01确认按钮.png", "24地下城01确认按钮", roiFull, fbSelf, [tl.RGBA])
#
# PCR['地下城:1层'] = tl(root, "24地下城11一层.png", "24地下城11一层", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:1/5'] = tl(root, "24地下城11一阶.png", "24地下城11一阶", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:2层'] = tl(root, "24地下城12二层.png", "24地下城12二层", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:2/5'] = tl(root, "24地下城12二阶.png", "24地下城12二阶", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:3层'] = tl(root, "24地下城13三层.png", "24地下城13三层", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:3/5'] = tl(root, "24地下城13三阶.png", "24地下城13三阶", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:4层'] = tl(root, "24地下城14四层.png", "24地下城14四层", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:4/5'] = tl(root, "24地下城14四阶.png", "24地下城14四阶", roiFull, fbSelf, [tl.RGBA])
#
# PCR['地下城:报酬窗口'] = tl(root, "24地下城02收取报酬.png", "24地下城02收取报酬", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:报酬确认'] = tl(root, "24地下城02确认按钮.png", "24地下城02确认按钮", roiFull, fbSelf, [tl.RGBA])
#
# PCR['地下城:5层'] = tl(root, "24地下城15五层.png", "24地下城15五层", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:5/5'] = tl(root, "24地下城15五阶.png", "24地下城15五阶", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城:撤退'] = tl(root, "24地下城16撤退.png", "24地下城16撤退", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城：撤退窗口'] = tl(root, "24地下城03撤退确认.png", "24地下城03撤退确认", roiFull, fbSelf, [tl.RGBA])
# PCR['地下城：撤退确认'] = tl(root, "24地下城03确认按钮.png", "24地下城03确认按钮", roiFull, fbSelf, [tl.RGBA])
#
# # ----------------------------------------------------------------
# #   探索 调查 流程
#
# PCR['探索:经验关卡'] = tl(root, "24探索01经验关卡.png", "24探索01经验关卡", roiFull, fbSelf, [tl.RGBA])
# PCR['探索:玛那关卡'] = tl(root, "24探索01玛那关卡.png", "24探索01玛那关卡", roiFull, fbSelf, [tl.RGBA])
# PCR['探索:关卡入口'] = tl(root, "24探索03关卡入口.png", "24探索03关卡入口", roiFull, fbSelf, [tl.RGBA])
# PCR['探索:前往经验'] = tl(root, "24探索04前往经验关卡按钮.png", "24探索04前往经验关卡按钮", roiFull, fbSelf, [tl.RGBA])
# PCR['探索:前往探索'] = tl(root, "24探索05前往探索首页按钮.png", "24探索05前往探索首页按钮", roiFull, fbSelf, [tl.RGBA])
#
# PCR['调查:圣迹'] = tl(root, "24调查01圣迹.png", "24调查01圣迹", roiFull, fbSelf, [tl.RGBA])
# PCR['调查:神殿'] = tl(root, "24调查02神殿.png", "24调查02神殿", roiFull, fbSelf, [tl.RGBA])
#
# # ----------------------------------------------------------------
# #   主线 活动 流程
#
# PCR['活动:活动关卡'] = tl(root, "24活动01活动关卡.png", "24活动01活动关卡", roiFull, fbSelf, [tl.RGBA])
# PCR['活动:首领挑战卷'] = tl(root, "24活动01首领挑战卷.png", "24活动01首领挑战卷", roiFull, fbSelf, [tl.RGBA])
#
# PCR['主线:普通'] = [
#     tl(root, "24主线01普通.png", "24主线01普通", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "24主线01普通选中.png", "24主线01普通选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['主线:困难'] = [
#     tl(root, "24主线02困难.png", "24主线02困难", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "24主线02困难选中.png", "24主线02困难选中", roiFull, fbSelf, [tl.RGBA])]
# PCR['主线:高难'] = [
#     tl(root, "24主线03高难.png", "24主线03高难", roiFull, fbSelf, [tl.RGBA]),
#     tl(root, "24主线03高难选中.png", "24主线03高难选中", roiFull, fbSelf, [tl.RGBA])]
#
# # ----------------------------------------------------------------
# #   竞技场 流程
#
# PCR['竞技场:收取'] = tl(root, "24竞技场01收取.png", "24竞技场01收取", roiFull, fbSelf, [tl.RGBA])
#
# PCR['竞技场:冷却完成'] = tl(root, "24竞技场01冷却完成.png", "24竞技场01冷却完成", roiFull, fbSelf, [tl.RGBA])
# PCR['竞技场:选择对手'] = tl(root, "24竞技场11选择对手.png", "24竞技场11选择对手", roiFull, fbSelf, [tl.RGBA])
# PCR['竞技场:编组时间'] = tl(root, "24竞技场12编组时间.png", "24竞技场12编组时间", roiFull, fbSelf, [tl.RGBA])
# PCR['竞技场:队伍123'] = tl(root, "24竞技场12队伍X.png", "24竞技场12队伍X", roiFull, fbSelf, [tl.RGBA])
# PCR['竞技场:战斗开始'] = tl(root, "24竞技场12战斗开始.png", "24竞技场12战斗开始", roiFull, fbSelf, [tl.RGBA])
# PCR['竞技场:跳过'] = tl(root, "24竞技场13跳过.png", "24竞技场13跳过", roiFull, fbSelf, [tl.RGBA])
# PCR['竞技场:下一步'] = tl(root, "24竞技场14下一步按钮.png", "24竞技场14下一步按钮", roiFull, fbSelf, [tl.RGBA])
#
# # ----------------------------------------------------------------
# #   通用 共享资源
#
# PCR['通用:返回'] = tl(root, "30全局01返回.png", "30全局01返回", roiFull, fbSelf, [tl.RGBA])
# PCR['通用:载入中'] = tl(root, "30通用01载入中.png", "30通用01载入中", roiFull, fbSelf, [tl.RGBA])


root = ".\\PCR1280720\\"
PCR = {
    # ----------------------------------------------------------------
    #   登录 流程
    '登录:点击屏幕'    : [
        tl(root, "00登录01点击屏幕.png", "00登录01点击屏幕", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "00登录01开始游戏.png", "00登录01开始游戏", roiFull, fbSelf, [tl.RGBA])],

    '登录:跳过'      : tl(root, "00登录02跳过按钮.png", "00登录02跳过按钮", roiFull, fbSelf, [tl.RGBA]),

    '帐号:切换'      : tl(root, "00登录02切换帐号.png", "00登录02切换帐号", roiFull, fbSelf, [tl.RGBA]),
    '账号:列表'      : tl(root, "01账号01列表按钮.png", "01账号01列表按钮", roiFull, fbSelf, [tl.RGBA]),
    '账号:上次'      : tl(root, "01账号01上次登录.png", "01账号01上次登录", roiFull, fbSelf, [tl.RGBA]),
    '账号:登录'      : tl(root, "01账号01登录按钮.png", "01账号01登录按钮", roiFull, fbSelf, [tl.RGBA]),

    '账号:取消'      : tl(root, "01账号04取消按钮.png", "01账号04取消按钮", roiFull, fbSelf, [tl.RGBA]),
    '账号:确认'      : tl(root, "01账号04确认按钮.png", "01账号04确认按钮", roiFull, fbSelf, [tl.RGBA]),

    '兰德索尔杯:选择角色' : tl(root, "02活动.兰德索尔杯.选择角色.png", "02活动.兰德索尔杯.选择角色", roiFull, fbSelf, [tl.RGBA]),
    '兰德索尔杯:旗帜'   : [
        tl(root, "02活动.兰德索尔杯.旗1.png", "02活动.兰德索尔杯.旗1", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "02活动.兰德索尔杯.旗2.png", "02活动.兰德索尔杯.旗2", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "02活动.兰德索尔杯.旗3.png", "02活动.兰德索尔杯.旗3", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "02活动.兰德索尔杯.旗4.png", "02活动.兰德索尔杯.旗4", roiFull, fbSelf, [tl.RGBA])],
    '兰德索尔杯:开始'   : tl(root, "02活动.兰德索尔杯.竞赛开始按钮.png", "02活动.兰德索尔杯.竞赛开始按钮", roiFull, fbSelf, [tl.RGBA]),
    '兰德索尔杯:跳过'   : tl(root, "02活动.兰德索尔杯.跳过按钮.png", "02活动.兰德索尔杯.跳过按钮", roiFull, fbSelf, [tl.RGBA]),
    '兰德索尔杯:结果'   : tl(root, "02活动.兰德索尔杯.结果.png", "02活动.兰德索尔杯.结果", roiFull, fbSelf, [tl.RGBA]),

    '通告:通知活动'    : [
        tl(root, "03通告01活动结束通告页面.png", "03通告01活动结束通告页面", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "03通告02通知页面.png", "03通告02通知页面", roiFull, fbSelf, [tl.RGBA])],
    '通告:关闭按钮'    : [
        tl(root, "03通告01关闭按钮.png", "03通告01取消按钮", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "03通告02关闭按钮.png", "03通告02取消按钮", roiFull, fbSelf, [tl.RGBA])],

    # ----------------------------------------------------------------
    #   游戏 路由 流程

    '导航:主页'      : [
        tl(root, "04导航01主页.png", "04导航01主页", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "04导航01主页选定.png", "04导航01主页选定", roiFull, fbSelf, [tl.RGBA])],
    '导航:角色'      : [
        tl(root, "04导航02角色.png", "04导航02角色", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "04导航02角色选定.png", "04导航02角色选定", roiFull, fbSelf, [tl.RGBA])],
    '导航:剧情'      : [
        tl(root, "04导航03剧情.png", "04导航03剧情", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "04导航03剧情选定.png", "04导航03剧情选定", roiFull, fbSelf, [tl.RGBA])],
    '导航:冒险'      : [
        tl(root, "04导航04冒险.png", "04导航04冒险", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "04导航04冒险选定.png", "04导航04冒险选定", roiFull, fbSelf, [tl.RGBA])],
    '导航:之家'      : [
        tl(root, "04导航05之家.png", "04导航05之家", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "04导航05之家选定.png", "04导航05之家选定", roiFull, fbSelf, [tl.RGBA])],
    '导航:抽卡'      : [
        tl(root, "04导航06抽卡.png", "04导航06抽卡", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "04导航06抽卡选中.png", "04导航06抽卡选中", roiFull, fbSelf, [tl.RGBA])],
    '导航:主菜单'     : [
        tl(root, "04导航07主菜单.png", "04导航07主菜单", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "04导航07主菜单选中.png", "04导航07主菜单选中", roiFull, fbSelf, [tl.RGBA])],

    '剧情:主线'      : tl(root, "04剧情01主线.png", "04剧情01主线", roiFull, fbSelf, [tl.RGBA]),
    '剧情:角色'      : tl(root, "04剧情02角色.png", "04剧情02角色", roiFull, fbSelf, [tl.RGBA]),
    '剧情:公会'      : tl(root, "04剧情03公会.png", "04剧情03公会", roiFull, fbSelf, [tl.RGBA]),
    '剧情:特别'      : tl(root, "04剧情04特别.png", "04剧情04特别", roiFull, fbSelf, [tl.RGBA]),
    '剧情:新内容'     : [
        tl(root, "04剧情05新内容.png", "04剧情05新内容", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "04剧情06新内容.png", "04剧情06新内容", roiFull, fbSelf, [tl.RGBA])],

    '公会之家:全部收取'  : tl(root, "04公会之家01全部收取按钮.png", "04公会之家01全部收取按钮", roiFull, fbSelf, [tl.RGBA]),

    '抽卡:每日标志'    : tl(root, "04抽卡01每日刷新.png", "04抽卡01每日刷新", roiFull, fbSelf, [tl.RGBA]),
    '抽卡:每日刷新'    : tl(root, "04抽卡02每日刷新.png", "04抽卡02每日刷新", roiFull, fbSelf, [tl.RGBA]),
    '抽卡:每日十连'    : tl(root, "04抽卡03每日十连.png", "04抽卡03每日十连", roiFull, fbSelf, [tl.RGBA]),

    '主页:商店'      : tl(root, "04按钮01商店.png", "04按钮01商店", roiFull, fbSelf, [tl.RGBA]),
    '主页:行会'      : tl(root, "04按钮02行会.png", "04按钮02行会", roiFull, fbSelf, [tl.RGBA]),
    '主页:通知'      : tl(root, "04按钮03通知.png", "04按钮03通知", roiFull, fbSelf, [tl.RGBA]),
    '主页:任务'      : tl(root, "04按钮04任务.png", "04按钮04任务", roiFull, fbSelf, [tl.RGBA]),
    '主页:礼物'      : tl(root, "04按钮05礼物.png", "04按钮05礼物", roiFull, fbSelf, [tl.RGBA]),

    # ----------------------------------------------------------------
    #   冒险 流程

    '冒险:主线'      : tl(root, "04冒险01主线.png", "04冒险01主线", roiFull, fbSelf, [tl.RGBA]),
    '冒险:探索'      : tl(root, "04冒险02探索.png", "04冒险02探索", roiFull, fbSelf, [tl.RGBA]),
    '冒险:地下城'     : tl(root, "04冒险03地下城.png", "04冒险03地下城", roiFull, fbSelf, [tl.RGBA]),
    '冒险:4调查'     : tl(root, "04冒险04调查.png", "04冒险04调查", roiFull, fbSelf, [tl.RGBA]),
    '冒险:团队战'     : tl(root, "04冒险05团队战.png", "04冒险05团队战", roiFull, fbSelf, [tl.RGBA]),
    '冒险:战斗竞技场'   : tl(root, "04冒险06战斗竞技场.png", "04冒险06战斗竞技场", roiFull, fbSelf, [tl.RGBA]),
    '冒险:公主竞技场'   : tl(root, "04冒险06公主竞技场.png", "04冒险06公主竞技场", roiFull, fbSelf, [tl.RGBA]),

    '冒险:露娜'      : tl(root, "04冒险07露娜之塔.png", "04冒险07露娜之塔", roiFull, fbSelf, [tl.RGBA]),
    '冒险:复刻'      : tl(root, "04冒险08复刻.png", "04冒险08复刻", roiFull, fbSelf, [tl.RGBA]),
    '冒险:活动'      : tl(root, "04冒险08活动.png", "04冒险08活动", roiFull, fbSelf, [tl.RGBA]),
    '冒险:外传'      : tl(root, "04冒险09外传.png", "04冒险09外传", roiFull, fbSelf, [tl.RGBA]),

    # ----------------------------------------------------------------
    #   商店 任务 礼物 流程

    '礼物:礼物箱'     : tl(root, "05礼物01礼物箱窗口.png", "05礼物01礼物箱窗口", roiFull, fbSelf, [tl.RGBA]),
    '礼物:全部收取'    : tl(root, "05礼物01全部收取按钮.png", "05礼物01全部收取按钮", roiFull, fbSelf, [tl.RGBA]),

    '任务:全部收取'    : tl(root, "05任务01全部收取.png", "05任务01全部收取", roiFull, fbSelf, [tl.RGBA]),
    '任务:关闭'      : tl(root, "05任务02关闭.png", "05任务02关闭", roiFull, fbSelf, [tl.RGBA]),

    '商店:购买确认'    : tl(root, "05商店01购买确认.png", "05商店01购买确认", roiFull, fbSelf, [tl.RGBA]),
    '商店:确认购买'    : tl(root, "05商店01确认购买.png", "05商店01确认购买", roiFull, fbSelf, [tl.RGBA]),
    '商店:卖空'      : tl(root, "05商店01卖空.png", "05商店01卖空", roiFull, fbSelf, [tl.RGBA]),
    '商店:通常售完'    : tl(root, "05商店01通常售完.png", "05商店01通常售完", roiFull, fbSelf, [tl.RGBA]),
    '商店:确认重置'    : tl(root, "05商店01确认重置.png", "05商店01确认重置", roiFull, fbSelf, [tl.RGBA]),

    '商店:通常'      : [
        tl(root, "05商店01通常.png", "05商店01通常", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "05商店01通常选中.png", "05商店01通常选中", roiFull, fbSelf, [tl.RGBA])],
    '商店:地下城'     : [
        tl(root, "05商店02地下城.png", "05商店02地下城", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "05商店02地下城选中.png", "05商店02地下城选中", roiFull, fbSelf, [tl.RGBA])],
    '商店:竞技场'     : [
        tl(root, "05商店03竞技场.png", "05商店03竞技场", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "05商店03竞技场选中.png", "05商店03竞技场选中", roiFull, fbSelf, [tl.RGBA])],
    '商店:公主'      : [
        tl(root, "05商店04公主竞技场.png", "05商店04公主竞技场", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "05商店04公主竞技场选中.png", "05商店04公主竞技场选中", roiFull, fbSelf, [tl.RGBA])],
    '商店:行会'      : [
        tl(root, "05商店05行会.png", "05商店05行会", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "05商店05行会选中.png", "05商店05行会选中", roiFull, fbSelf, [tl.RGBA])],
    '商店:大师'      : [
        tl(root, "05商店06大师.png", "05商店06大师", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "05商店06大师选中.png", "05商店06大师选中", roiFull, fbSelf, [tl.RGBA])],
    '商店:秘石'      : [
        tl(root, "05商店07秘石.png", "05商店07秘石", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "05商店07秘石选中.png", "05商店07秘石选中", roiFull, fbSelf, [tl.RGBA])],
    '商店:限定'      : [
        tl(root, "05商店08限定.png", "05商店08限定", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "05商店08限定选中.png", "05商店08限定选中", roiFull, fbSelf, [tl.RGBA])],

    '商店:选框'      : [
        tl(root, "05商店10批量选框.png", "05商店10批量选框", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "05商店10批量选框半.png", "05商店10批量选框半", roiFull, fbSelf, [tl.RGBA])],
    '商店:十万更新'    : tl(root, "05商店11十万立刻更新.png", "05商店11十万立刻更新", roiFull, fbSelf, [tl.RGBA]),
    '商店:立刻更新'    : tl(root, "05商店12立刻更新.png", "05商店12立刻更新", roiFull, fbSelf, [tl.RGBA]),
    '商店:批量购入'    : tl(root, "05商店12批量购入.png", "05商店12批量购入", roiFull, fbSelf, [tl.RGBA]),
    '商店:超级经验'    : tl(root, "05商店20超级经验药剂.png", "05商店20超级经验药剂", roiFull, fbSelf, [tl.RGBA]),

    # ----------------------------------------------------------------
    #   战斗 流程

    '战斗:下一关'     : [
        tl(root, "11战斗01下一关.png", "11战斗01下一关", roiFull, cal(mo.SELF, -50, 90, 100, 90), [tl.RGBA]),
        tl(root, "11战斗01下一关箭头.png", "11战斗01下一关箭头", roiFull, cal(mo.SELF, -50, 80, 100, 90), [tl.RGBA])],
    '战斗:下一关备用'   : [
        tl(root, "11战斗01下一关GM.png", "11战斗01下一关GM", roiFull, cal(mo.SELF, -30, 65, 60, 30), [tl.RGBA]),
        tl(root, "11战斗01下一关SSH.png", "11战斗01下一关SSH", roiFull, cal(mo.SELF, -30, 65, 60, 30), [tl.RGBA])],

    '战斗:关卡横杠'    : tl(root, "11战斗01关卡横杠.png", "11战斗01关卡横杠", roiFull, fbSelf, [tl.RGBA]),
    # '战斗:一星'      : tl(root, "11战斗01一心.png", "11战斗01一心", roiFull, fbSelf, [tl.RGBA]),
    # '战斗:二星'      : tl(root, "11战斗01二心.png", "11战斗01二心", roiFull, fbSelf, [tl.RGBA]),
    # '战斗:三星'      : tl(root, "11战斗01三心.png", "11战斗01三心", roiFull, fbSelf, [tl.RGBA]),
    # '战斗:满星'      : tl(root, "11战斗01满心.png", "11战斗01满心", roiFull, fbSelf, [tl.RGBA]),

    '战斗:通关星'     : [
        tl(root, "11战斗01满星.png", "11战斗01满星", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "11战斗01一星.png", "11战斗01一星", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "11战斗01二星.png", "11战斗01二星", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "11战斗01三星.png", "11战斗01三星", roiFull, fbSelf, [tl.RGBA]),
    ],

    '战斗:次数用完'    : tl(root, "11战斗01次数用完.png", "11战斗01次数用完", roiFull, fbSelf, [tl.RGBA]),
    '战斗:上一关卡'    : tl(root, "11战斗01上一关卡.png", "11战斗01上一关卡", roiFull, fbSelf, [tl.RGBA]),
    '战斗:下一关卡'    : tl(root, "11战斗01下一关卡.png", "11战斗01下一关卡", roiFull, fbSelf, [tl.RGBA]),

    '扫荡:批量'      : tl(root, "10扫荡01批量.png", "10扫荡01批量", roiFull, fbSelf, [tl.RGBA]),
    '扫荡:一键扫荡'    : tl(root, "10扫荡02一键扫荡按钮.png", "10扫荡02一键扫荡按钮", roiFull, fbSelf, [tl.RGBA]),
    '扫荡:加'       : tl(root, "10扫荡03加号.png", "10扫荡03加号", roiFull, fbSelf, [tl.RGBA]),
    '扫荡:使用'      : [
        tl(root, "10扫荡03击破.png", "10扫荡03击破", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "10扫荡03使用.png", "10扫荡03使用", roiFull, fbSelf, [tl.RGBA])],
    '扫荡:扫荡确认'    : tl(root, "10扫荡03确认.png", "10扫荡03确认", roiFull, fbSelf, [tl.RGBA]),

    '扫荡:完成确认'    : tl(root, "10扫荡05确认.png", "10扫荡05确认", roiFull, fbSelf, [tl.RGBA]),
    '扫荡:合计获得'    : tl(root, "10扫荡04合计获得报酬.png", "10扫荡04合计获得报酬", roiFull, fbSelf, [tl.RGBA]),
    '扫荡:跳过完毕'    : tl(root, "10扫荡05跳过完毕.png", "10扫荡05跳过完毕", roiFull, fbSelf, [tl.RGBA]),

    '战斗:挑战按钮'    : tl(root, "11战斗01挑战按钮.png", "11战斗01挑战按钮", roiFull, fbSelf, [tl.RGBA]),
    '战斗:挑战取消'    : tl(root, "11战斗01取消按钮.png", "11战斗01取消按钮", roiFull, fbSelf, [tl.RGBA]),
    '战斗:体力不足'    : tl(root, "11战斗01体力不足.png", "11战斗01体力不足", roiFull, fbSelf, [tl.RGBA]),

    '战斗:队伍编组'    : tl(root, "11战斗02队伍编组.png", "11战斗02队伍编组", roiFull, fbSelf, [tl.RGBA]),
    '战斗:空队伍'     : [
        tl(root, "11战斗02空队伍.png", "11战斗02空队伍", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "11战斗02空队伍无条.png", "11战斗02空队伍无条", roiFull, fbSelf, [tl.RGBA])],
    '战斗:我的队伍'    : tl(root, "11战斗02我的队伍.png", "11战斗02我的队伍", roiFull, fbSelf, [tl.RGBA]),
    '战斗:队伍一览'    : tl(root, "11战斗02队伍一览.png", "11战斗02队伍一览", roiFull, fbSelf, [tl.RGBA]),
    '战斗:使用编组'    : tl(root, "11战斗02使用编组.png", "11战斗02使用编组", roiFull, fbSelf, [tl.RGBA]),
    '战斗:战斗开始'    : tl(root, "11战斗02战斗开始.png", "11战斗02战斗开始", roiFull, fbSelf, [tl.RGBA]),

    '战斗:时间沙漏'    : tl(root, "11战斗03沙漏.png", "11战斗03沙漏", roiFull, fbSelf, [tl.RGBA]),
    '对话:名片'      : tl(root, "12对话01.png", "12对话01", roiFull, fbSelf, [tl.RGBA]),
    '对话:箭头'      : tl(root, "12对话02.png", "12对话02", roiFull, fbSelf, [tl.RGBA]),

    '地下城:胜利'     : tl(root, "24地下城02胜利.png", "24地下城02胜利", roiFull, fbSelf, [tl.RGBA]),
    '战斗:挑战胜利'    : tl(root, "11战斗03挑战胜利.png", "11战斗03挑战胜利", roiFull, fbSelf, [tl.RGBA]),
    '战斗:玩家等级'    : tl(root, "11战斗03玩家等级.png", "11战斗03玩家等级", roiFull, fbSelf, [tl.RGBA]),
    '战斗:好感度'     : tl(root, "11战斗03好感度.png", "11战斗03好感度", roiFull, fbSelf, [tl.RGBA]),

    '战斗:限定商店'    : tl(root, "11战斗03限定商店.png", "11战斗03限定商店", roiFull, fbSelf, [tl.RGBA]),
    '战斗:商店取消'    : tl(root, "11战斗03取消.png", "11战斗03取消", roiFull, fbSelf, [tl.RGBA]),
    '战斗:获得道具'    : tl(root, "11战斗03获得道具.png", "11战斗03获得道具", roiFull, fbSelf, [tl.RGBA]),
    '战斗:下一步'     : tl(root, "11战斗03下一步.png", "11战斗03下一步", roiFull, fbSelf, [tl.RGBA]),

    '战斗:自动'      : tl(root, "11战斗03自动.png", "11战斗03自动", roiFull, fbSelf, [tl.RGBA]),
    '战斗:一倍'      : tl(root, "11战斗03一倍.png", "11战斗03一倍", roiFull, fbSelf, [tl.RGBA]),
    '战斗:二倍'      : tl(root, "11战斗03二倍.png", "11战斗03二倍", roiFull, fbSelf, [tl.RGBA]),
    '战斗:三倍'      : tl(root, "11战斗03三倍.png", "11战斗03三倍", roiFull, fbSelf, [tl.RGBA]),

    # ----------------------------------------------------------------
    #   地下城 流程

    '地下城:剩余次数'   : tl(root, "24地下城01剩余挑战次数.png", "24地下城01剩余挑战次数", roiFull, fbSelf, [tl.RGBA]),
    '地下城:次数0/1'  : tl(root, "24地下城01零一.png", "24地下城01零一", roiFull, fbSelf, [tl.RGBA]),
    '地下城:次数1/1'  : tl(root, "24地下城01一一.png", "24地下城01一一", roiFull, fbSelf, [tl.RGBA]),

    '地下城:EX3'    : tl(root, "24地下城EX3.png", "24地下城EX3", roiFull, fbSelf, [tl.RGBA]),
    '地下城:确认地域'   : tl(root, "24地下城01确认按钮.png", "24地下城01确认按钮", roiFull, fbSelf, [tl.RGBA]),

    '地下城:1层'     : tl(root, "24地下城11一层.png", "24地下城11一层", roiFull, fbSelf, [tl.RGBA]),
    '地下城:1/5'    : tl(root, "24地下城11一阶.png", "24地下城11一阶", roiFull, fbSelf, [tl.RGBA]),
    '地下城:2层'     : tl(root, "24地下城12二层.png", "24地下城12二层", roiFull, fbSelf, [tl.RGBA]),
    '地下城:2/5'    : tl(root, "24地下城12二阶.png", "24地下城12二阶", roiFull, fbSelf, [tl.RGBA]),
    '地下城:3层'     : tl(root, "24地下城13三层.png", "24地下城13三层", roiFull, fbSelf, [tl.RGBA]),
    '地下城:3/5'    : tl(root, "24地下城13三阶.png", "24地下城13三阶", roiFull, fbSelf, [tl.RGBA]),
    '地下城:4层'     : tl(root, "24地下城14四层.png", "24地下城14四层", roiFull, fbSelf, [tl.RGBA]),
    '地下城:4/5'    : tl(root, "24地下城14四阶.png", "24地下城14四阶", roiFull, fbSelf, [tl.RGBA]),

    '地下城:报酬窗口'   : tl(root, "24地下城02收取报酬.png", "24地下城02收取报酬", roiFull, fbSelf, [tl.RGBA]),
    '地下城:报酬确认'   : tl(root, "24地下城02确认按钮.png", "24地下城02确认按钮", roiFull, fbSelf, [tl.RGBA]),

    '地下城:5层'     : tl(root, "24地下城15五层.png", "24地下城15五层", roiFull, fbSelf, [tl.RGBA]),
    '地下城:5/5'    : tl(root, "24地下城15五阶.png", "24地下城15五阶", roiFull, fbSelf, [tl.RGBA]),
    '地下城:撤退'     : tl(root, "24地下城16撤退.png", "24地下城16撤退", roiFull, fbSelf, [tl.RGBA]),
    '地下城:撤退窗口'   : tl(root, "24地下城03撤退确认.png", "24地下城03撤退确认", roiFull, fbSelf, [tl.RGBA]),
    '地下城:撤退确认'   : tl(root, "24地下城03确认按钮.png", "24地下城03确认按钮", roiFull, fbSelf, [tl.RGBA]),

    # ----------------------------------------------------------------
    #   探索 调查 流程

    '探索:零次0/X'   : tl(root, "24探索01零次.png", "24探索01零次", roiFull, fbSelf, [tl.RGBA]),
    '探索:经验关卡'    : tl(root, "24探索01经验关卡.png", "24探索01经验关卡", roiFull, fbSelf, [tl.RGBA]),
    '探索:玛那关卡'    : tl(root, "24探索01玛那关卡.png", "24探索01玛那关卡", roiFull, fbSelf, [tl.RGBA]),
    '探索:关卡入口'    : tl(root, "24探索03关卡入口.png", "24探索03关卡入口", roiFull, fbSelf, [tl.RGBA]),
    '探索:前往经验'    : tl(root, "24探索04前往经验关卡按钮.png", "24探索04前往经验关卡按钮", roiFull, fbSelf, [tl.RGBA]),
    '探索:前往探索'    : tl(root, "24探索05前往探索首页按钮.png", "24探索05前往探索首页按钮", roiFull, fbSelf, [tl.RGBA]),

    '调查:圣迹'      : tl(root, "24调查01圣迹.png", "24调查01圣迹", roiFull, fbSelf, [tl.RGBA]),
    '调查:神殿'      : tl(root, "24调查02神殿.png", "24调查02神殿", roiFull, fbSelf, [tl.RGBA]),

    # ----------------------------------------------------------------
    #   主线 活动 流程

    '活动:活动关卡'    : tl(root, "24活动01活动关卡.png", "24活动01活动关卡", roiFull, fbSelf, [tl.RGBA]),
    '活动:首领挑战卷'   : tl(root, "24活动01首领挑战卷.png", "24活动01首领挑战卷", roiFull, fbSelf, [tl.RGBA]),

    '主线:普通'      : [
        tl(root, "24主线01普通.png", "24主线01普通", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "24主线01普通选中.png", "24主线01普通选中", roiFull, fbSelf, [tl.RGBA])],
    '主线:困难'      : [
        tl(root, "24主线02困难.png", "24主线02困难", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "24主线02困难选中.png", "24主线02困难选中", roiFull, fbSelf, [tl.RGBA])],
    '主线:高难'      : [
        tl(root, "24主线03高难.png", "24主线03高难", roiFull, fbSelf, [tl.RGBA]),
        tl(root, "24主线03高难选中.png", "24主线03高难选中", roiFull, fbSelf, [tl.RGBA])],

    # ----------------------------------------------------------------
    #   竞技场 流程

    '竞技场:收取'     : tl(root, "24竞技场01收取.png", "24竞技场01收取", roiFull, fbSelf, [tl.RGBA]),

    '竞技场:冷却完成'   : tl(root, "24竞技场01冷却完成.png", "24竞技场01冷却完成", roiFull, fbSelf, [tl.RGBA]),
    '竞技场:选择对手'   : tl(root, "24竞技场11选择对手.png", "24竞技场11选择对手", roiFull, fbSelf, [tl.RGBA]),
    '竞技场:编组时间'   : tl(root, "24竞技场12编组时间.png", "24竞技场12编组时间", roiFull, fbSelf, [tl.RGBA]),
    '竞技场:队伍123'  : tl(root, "24竞技场12队伍X.png", "24竞技场12队伍X", roiFull, fbSelf, [tl.RGBA]),
    '竞技场:战斗开始'   : tl(root, "24竞技场12战斗开始.png", "24竞技场12战斗开始", roiFull, fbSelf, [tl.RGBA]),
    '竞技场:跳过'     : tl(root, "24竞技场13跳过.png", "24竞技场13跳过", roiFull, fbSelf, [tl.RGBA]),
    '竞技场:下一步'    : tl(root, "24竞技场14下一步按钮.png", "24竞技场14下一步按钮", roiFull, fbSelf, [tl.RGBA]),

    # ----------------------------------------------------------------
    #   通用 共享资源

    '通用:返回'      : tl(root, "30全局01返回.png", "30全局01返回", roiFull, fbSelf, [tl.RGBA]),
    '通用:载入中'     : tl(root, "30通用01载入中.png", "30通用01载入中", roiFull, fbSelf, [tl.RGBA]),
}

print()
