# Helper 
     一个使用Python编写，基于OpenCV的画面内容识别算法项目
     该项目还处于初级开发阶段，任何功能函数方法都具有不确定的变更，但会尽可能的不变更函数调用方式
     
     为了防止大量使用，提供使用门槛，延长该项目活在光明下的时间
     下面的说明与教程会写得一塌糊涂，其实就目前的完成度也没写太好的必要
     
     目前仅支持MEMU，理论上支持其他模拟器、安卓实体机，但要修改部分脚本
     (测试通过于 MEMU安卓分辨率1920x1080 系统分辨率3840x2160 系统缩放200%)
     
### 警告 该项目几乎违反所有网络游戏或网络软件的用户协议!
     仅允许个人以学习为目的使用 禁止用于任何商用盈利违法等用途
     因使用本项目 产生的一切问题后果由使用者自行承担 产生的任何法律后果由使用者自行承担
     
     后果包括但不限于：游戏封禁或回档、账户拉黑或锁定、违法相关法律法规被起诉
 
### 用户自定义脚本

     自行编写的建议结构
          import ...
          
          函数1 : ...
          ...
          函数N : ...
          
          主循环 : ...
          
          定义安卓模拟器
          ...
          
          初始化循环选择器
          ...
          
          循环入口 : ...
     
#### 1.制作图像匹配资源
     1.0 关于分辨率的问题
          (!)本项目CV处理的图像分辨率和安卓实际分辨率不一样，默认是1280x720，可在*Env.py里修改
          (!)安卓模拟器的分辨率是1920x1080，但模拟器窗口显示虚拟机画面的分辨率，在获取画面时会被设置为1280x720
             也就是制作匹配资源的全程都以分辨率1280x720为准，算法会解决映射到模拟器1920x1080的问题
          (!)在*Env.py里有一个cv缩放倍率cvScale，模板匹配成功后会缩放到模拟器1920x1080的触摸坐标

     1.1 修改*Win32.py脚本 
          (1)if __name__ == '__main__' : 内的 VM = GetVMScreen(title='VM')
             把 title='VM' 的 VM 改为目标模拟器的窗口标题，可在任务管理器里看到这个标题
          (2)save = 'debug\\' + time.strftime('%Y%m%d.%H%M%S', time.localtime(time.time()))[2 :] + '.tif'
             'debug\\' 的 debug 为保存截图的文件夹，可以修改，若不存在需要自行建立
          (3)执行*Win32.py脚本后，若修改正确会在保存文件就里看到一个以时间为文件名的tif图像文件

     1.2 裁剪被识别图像模板
          (0)本教程以Photoshop为主，且不会过多强调在PS里如何操作
             也可以使用其他支持 选区 图层 辅助线 快速导出图层 的二维图像编辑工具
          (1)使用选区尽可能大的选定 被识别图像区域，切记不要包含其他无关内容，除非没办法了或使用透明图像匹配
             若必须使用透明图像匹配的模板，给模板的图层加蒙版，然后使用铅笔黑色画掉希望透明的区域
             例如要选找 [圆角的确定按钮]，就矩形选择 [圆角的确定按钮] 但不包含左右两边的圆角部分
          (2)然后Ctrl+J拷贝图层，会得到一个新图层，双击它的文字重命名为方便后期寻找的名字，
             例如 01某界面01某按钮，可以让资源管理器按照前面的数字顺序排列显示文件，方便寻找图像
          (3)然后选定背景图层，选下一个模板再Ctrl+J拷贝图层得到所有需要的图像模板，不选背景图层就Ctrl+J空气了
          (4)重复123到所有希望使用的模板都选完
          (5)最后按住Ctrl选择所有模板图层，右键快速导出为PNG，在保存的文件夹可以看到导出的图像
          (6)保存tif文件，方便以后修改，默认设置的tif会记住图层
          
     1.3 在脚本里定义模板
          (0)定义模板的目的是在一个对象里保存模板的图像、感兴趣区域、模拟触摸区域、注释信息、文件读取模式等
          (1)使用definetl(图像文件集根目录, 图像文件路径, 文本注释, 感兴趣区域, 反馈触摸区域, [读取模式])
             例如 definetl('.\\AAAA\\', 'Image.png', 'xxxxx', ...)
          (2)读取模式支持 definetl.RGBA definetl.RGB definetl.Gray 必须套一层[]传参
             例如 definetl(... ,[definetl.RGBA])
          (3)感兴趣区域为元组(X1,Y1,X2,Y2)仅绝对区域，预设支持*Env.py内 roiFull(匹配0，0到1280,720全图)
             例如 definetl(... , (0, 0, 1280, 720), (0, 0, 1280, 720), ...)
          (!)相对区域使用*Env.py内cal(pos0, mv1, mv2, mv3, mv4)函数，其中pos0为*Env.py内mo(Enum)枚举，
             传入pos0=mo.SELF可配置为：匹配成功的坐标为原点，经过mv1,mv2移动后，大小为宽mv3高mv4的区域
             相似的，传入mo.LT则是图像左上角(Left-Top)为原点，mo.RB则是图像右下角(Right-Bottom)为原点
          (4)反馈触摸区域为元组(X1,Y1,X2,Y2)可以为相对区域，预设支持*Env.py内 fbNone(不点任何区域) fbSelf(点击自己)
             例如 definetl(... , cal(mo.SELF, -50, 90, 100, 90), ...) 
          (!)可以在PS裁剪模板的时候，通过参考线或选区得到相应的像素坐标
          
     1.4 巧用字典
          (0)字典的键值为字符串，可以使用英文之外的字符命名模板类，让后面写的自动化逻辑更清晰，例如
             root = ".\\root\\"
             demo = {
               '中文:名字1' : [
                    tl(root, "1.png", "xxxx1", roiFull, fbSelf, [tl.RGBA]),
                    tl(root, "2.png", "xxxx2", roiFull, fbSelf, [tl.RGBA])],
               '中文:名字2' : tl(root, "3.png", "xxxx3", roiFull, fbSelf, [tl.RGBA]),
             }
             识别算法(... ,demo['中文:名字1'] , ...) # 传入模板类组，匹配第一个失败就匹配第二个，以此类推
             识别算法(... ,demo['中文:名字1'][1] , ...) # 传入模板类组的第二个模板类
             识别算法(... ,demo['中文:名字2'] , ...) # 传入模板类组
             
     1.5 模板类对象
          (0)成员列表
             .array 图像内容
             .ROI 感兴趣区域
             .FB 触摸反馈区域
             .alpha 透明蒙版，不透明图像为None
             .space 颜色空间，参考[读取模式]
             .width 图像宽度
             .height 图像高度
             
           (1)得到引入随机的反馈坐标
              使用*Env.py内GetFBXY(xy,tl)函数，xy为元组(x,y)
              tl可以为模板类对象，或元组(x1,x2,y1,y2)，或*Env.py内cal()的返回值
              例如 XY = GetFBXY(XY, tl=tl)
              使用随机可降低被反作弊或机器人检测发现的概率
              
#### 2.基本功能函数
     2.0 基本逻辑
         逻辑就是这个自定义脚本是怎么工作的，例如模板匹配成功后该怎么做，做完后该干什么
         安卓模拟器和应用的运行状态是未知的，可能会卡顿。如果卡顿了，模拟触摸可能会没有效果
         这时就需要一种反馈逻辑：识别(按钮) → 成功该干什么(点击按钮) → 干了有什么现象(按钮消失或某东西出现) → 完成
         这一条逻辑里涉及四个算法：图像识别、虚拟触摸、等待消失、等待出现，这四个算法本项目已经提供示例
         
     2.1 图像识别
         在*.MATCH.py里提供了三个函数封装和一个枚举
            mt(Enum) 匹配函数功能开关，套[]传入param
            matchtl(screen, tlclass, threshold=0.8, param=None) 自动匹配函数，自动选择mask()或rect()
            mask(screen, tlclass, threshold=0.8, param=None) 透明匹配函数
            rect(screen, tlclass, threshold=0.8, param=None) 矩形匹配函数
         统一参数 screen 为被识别背景，tlclass 为模板类列表或模板类，threshold 为识别成功阈值
         param 为功能开关，例如 mt.rgb为彩色识别(默认灰度)，可以使用列表同时传入多个开关，如果函数不支持会直接舍弃
         例如 xy = matchtl(mu.GetScreen(), tl, threshold, [mt.quiet]) # 为静默不输出日志匹配
         其中 matchtl() 支持 模板类列表 输入 和 直接模板类 输入，mask()与rect()只支持直接模板类输入无法遍历列表
         建议直接使用 matchtl() 自动根据有无透明图层进行匹配
         
     2.2 虚拟触摸
         在*.Event.py里提供一个类用于定义安卓模拟器设备，且应该在脚本主循环之前定义
             mudevice(addr, title, inputdev)
         参数 addr 是模拟器ADB网络IP地址端口，title 为模拟器实例窗口标题，inputdev 为触摸设备事件地址
         使用 mudevice.inputTouch(xy, endSleep) 方法进行虚拟触摸
     
     2.3 等待消失和出现
         等待少不了一个词超时，可以使用 while True 死循环实现等待，在进入死循环之前计算好超时时刻
         例如 break_time = datetime.datetime.now() + datetime.timedelta(seconds=abs(timeout + 1) / 1000)
         在死循环中增加超时判断强制打断死循环返回等待超时，同时还要兼顾无超时设计一直等待出现
         例如 if timeout != 0 and datetime.datetime.now().__gt__(break_time) : return False
         判断消失或出现的实现，其中 xyFalse 是*Env.py内预设的识别失败标志
         出现 if xyFalse != matchtl(mu.GetScreen(), tl, threshold, [mt.quiet]) : return True
         消失 if xyFalse == matchtl(mu.GetScreen(), tl, threshold, [mt.quiet]) : return True
         
#### 3.死循环路由系统
     3.0 路由系统
         简单的循环匹配逻辑没有必要使用路由系统，但复杂匹配逻辑就需要路由系统指导每个函数的死循环内执行哪一段代码
         例如 while True : 
                while flag==1 : ...
                while flag==2 : ...
                while flag==3 : ...
         其中1 2 3对应的是不同的阶段，该使用什么识别组合，关闭不必要的算法提高脚本的实时性
         以及防止相似场景的错误匹配成功，例如两个场景都有一样的确认按钮，但功能完全不同甚至相反
         
     3.1 根路由检测
         跟路由指的是子路由的集合，比如 16位整数变量的高八位一样，则判断为一个分类的路由
         该操作可以保证进入正确的死循环，例如刷两个类型的本，如果没刷到第二个副本
         但脚本因某些问题进入第二个副本了，由于跟路由检测失败会马上退出循环回到第一个
         该项目提供了路由标志类的示例和成员方法 
             class FlagInit(flagNum, flagNote='L', base=0)
                   .flag = base << 8 | flagNum # 路由标志
         参数 flagNum 为唯一路由需要，一个根路由内不允许出现两个一模一样的标志，八位足以容纳255个标志
         参数 flagNote 为标志注释，方便脚本调试和定位执行位置，以供意外情况下人工引导恢复执行
         参数 base 为根路由标识，整个自定义脚本作用域内不允许出现重复的根路由标识，八位足以容纳255个根路由
         使用时应该准备一个全局变量保存当前的路由信息，例如
             GlobalFlag = None
             baseXXXXH8 = 0xAF
             flagXXX1 = FlagInit(1, 'note', baseXXXXH8)
             GlobalFlag = flagXXX1.flag
             while True :
                while ... : ...
                while GlobalFlag == flagXXX1.flag : ...
                while ... : ...
      
      3.2 导航记录
          把保存路由信息的全局变量扩展成对象并加入方法
             class FlagCtrl(flag)    # flag 为初始化标志
                   .get()            # 获取当前标志
                   .note()           # 获取当前标志的注释
                   .isBase(base)     # 判断当前标志是否属于传入base分类
                   .set(flag, param) # 改变当前标志并更新导航信息
                   .IS(flag)         # 判断当前标志是否等于传入flag
          其中.set(flag, param)的 param 可传入控制符 .pop出栈 .push入栈 .root设置根 .sw切换标志
          需要重置导航 .root，结果 /根
          在进入页面时 .push 压入一层导航，结果 /根/操作1
          页面又进又出 .sw 切换同层导航，结果 /根/操作2
          完成退出页面 .pop 弹出一层导航，结果 /根
          
         
#### 用于学习该项目的功能模板
          基于 MEMU 测试开发的 [公主连结Re:Dive简体服] 小号每日内容自动辅助脚本
          目前仅稍稍完善了 地下城AutoDungeon(MEMU) 下一关AutoNextLevel(MEMU)，需要自行编辑脚本切换
          警告 该自定义脚本违反 上海宽娱数码科技有限公司运营的游戏(公主连结Re:Dive)内发布的游戏公平运营声明 如下链接
          ![image](https://user-images.githubusercontent.com/15169084/165489327-bdeff184-9d93-433a-a63f-47055934f484.png)
          使用者自行承担一切后果。本项目若收到该游戏运营方删除该自定义脚本的要求，会移除该自定义脚本及图像资源。
     
### 依赖&调用 (当前仅支持Windows环境)
     平台接口：pywin32 win32gui
     图像处理：opencv-python Pillow numpy
     日志输出：colorama colorlog
     可能移除：keyboard
     Pip自动安装 pip install -r requirements
     
### 功能&实现

#### 　 定义安卓设备类
     用于定义模拟安卓设备的类 
     *Event.py 内提供了如下类与方法
     　  定义安卓模拟器 mudevice(addr=Adb控制IP地址端口, title=模拟器窗口标题, inputdev=触摸事件输入地址)
     　  连接设备 mudevice.connect()
         发送指令 mudevice.command(单行shell指令)
         发送事件 mudevice.sendevent(事件列表)
         调试触摸 mudevice.inputTouch(数组(x,y), 结束延迟)
         事件触摸 mudevice.eventTouch(数组(x,y), 按压时间, 重复次数, 每次结束延迟)
           ↑ 实验性，存在adb反应慢，某些应用内无法完成单击的问题
         获取屏幕 mudevice.GetScreen()
         
#### 　 获取Windows窗口画面
     窗口必须前台 (可以被遮挡 可以在其他桌面 不能最小化)
     *Win32.py 内提供了如下函数
     　  获取系统内所有窗口   GetWinHandler()
     　  获取安卓模拟器句柄   GetMuHandler()
     　  获取安卓模拟器画面   GetVMScreen(title=句柄标题,Mu='MEMU')
     在自定义用户python脚本内的使用方式为 定义安卓设备前
     　  ... 预运行部分 ...
     　  GetMuHandler() # 获取可选的模拟器实例列表 (正在完善，可以匹配到黑名单外的所有QT外壳窗口，但不影响后期使用)
     　  ... 安卓设备定义 ...
        
#### 　 自定义脚本资源定义
     用于定义被查找图像的类
     *Env.py 内提供了如下类与方法
     　  定义资源 definetl(图像文件集根目录, 图像文件路径, 文本注释, 感兴趣区域, 反馈触摸区域, [读取模式])
                 例如 自定义脚本的资源存放于 AAAA文件夹下：definetl('.\\AAAA\\', 'Image.png', 'xxxxx', ....)
                 感兴趣区域与反馈触摸区域 元组(X1,Y1,X2,Y2) 是基于CV算法分辨率的像素区域
                 例如1280x720的算法分辨率，只对左上角100,100到200,200区域进行图像匹配：(100,100,200,200)
                 只对150,150到250,250区域内进行安卓模拟点击 (150,150,250,250)，实际使用需要缩放回模拟器的实际坐标
