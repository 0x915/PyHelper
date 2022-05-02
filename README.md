# Helper

    一个使用Python编写，基于OpenCV的画面内容识别算法项目
    该项目还处于初级开发阶段，任何功能函数方法都有变更的可能
    (但会尽可能的只进行内部变更，不改变函数调用方式)
     
    为了延长该项目活在光明下的时间，请勿公开使用与降低使用门槛
     
    已实现基本功能：
        1. 基于cv2.matchTemplate的图像匹配(支持有明显特征的RGB透明模板)
        2. 图像模板对象(类封装ROI区域、反馈区域、色彩空间、长宽通道信息)
        3. 安卓adb触摸调试输入(tap)与触摸事件输入(sendevent)
        4. Windows窗口句柄截图(目标窗口不可最小化)
        5. 调试运行日志输出
    
    已实现核心功能：
        1. 块作用域 临时只让特定while/if内的代码执行
        2. 导航系统 显示当前代码执行位置与保存作用域标识
        2. 检测目标 是否存在
        3. 目标出现 是否在超时前出现
        4. 目标消失 是否在超时前消失
        5. 点击目标 是否在超时前响应出现/消失动作

    待实现功能：
        1. 其他模拟器支持(当前测试通过为MEMU)
        2. Windows缩放支持(已适配缩放的模拟器窗口尺寸会随之改变)
        3. 图像匹配的ROI功能实装
     
     当前测试通过于：
        1. 系统 分辨率3840x2160 缩放200%
        2. MEMU 安卓分辨率1920x1080 窗口分辨率1280x750

### 警告 该项目几乎违反所有网络游戏或网络软件的用户协议!

     仅允许个人以学习为目的使用 禁止用于任何商用盈利违法等用途
     因使用本项目产生的 一切问题后果任何法律后果 由使用者自行承担
     后果包括但不限于：游戏封禁或回档、账户拉黑或锁定、违法相关法律法规被起诉

### 用户自定义脚本

    使用者对特定安卓软件编写的自动化操作脚本，建议的结构：

        import ...

        def func1() : ... # 自定义函数，例如完成某个大操作的运行逻辑

        def func2() : ... # 更多自定义函数，完成其他大操作的运行逻辑

        def funcX() : ... # 可以是嵌套组合了其他自定义函数的运行逻辑

        def main() : # 主函数，执行各自定义函数的次序或开关
            ...
            funcX() 
            ...

        ... # 定义 安卓设备 (全局对象)

        ... # 初始化 块作用域选择器 (全局对象)

        if __name__ == '__main__' :
            while True :  
                ... 
                main() # 主循环，执行main()或处理异常
                ...

    编写前，要先准备用途图像匹配的外部模板文件，大概的步骤为：
        1. 使用本项目的 句柄截图功能 截取模拟器画面
        2. 使用图像软件 切割制作模板图像 并适当命名保存
        3. 使用本项目的 模板类 在自定义脚本里定义模板对象
        4. 使用本项目的 图像匹配函数 测试定义的模板对象(同时测试模板图像)

#### 1.制作图像匹配资源

    1.0 关于分辨率的问题
        (!)本项目 CV处理图像分辨率 和 安卓显示分辨率 不一样
           *public.py文件内：
                dvWidth dvHeight -> 物理分辨率(往显示器输出的)
                uiWidth uiHeight -> 逻辑分辨率(系统界面缩放后)
                muTitle -> 模拟器窗口的标题高度 (默认30px/200%缩放)
                muWidth muHeight -> 模拟器窗口大小(根据系统缩放计算)
                cvWidth cvHeight -> cv处理分辨率(默认1280x720)
                vmWidth vmHeight -> 安卓显示分辨率(默认1920x1080)
                cvScale = vmHeight/cvHeight -> cv处理结果映射到安卓分辨率的倍率
           获取安卓画面的流程：
                会先把模拟器窗口设定为 宽(muWidth) 高(muHeight+muTitle)
                定位到画面渲染子句柄(安卓虚拟机画面输出的地方)
                使用win32api截图子句柄的图形并转换为cv格式返回
                (兼容性问题：不同模拟器的渲染子句柄相对位置与标题可能不一样)
           *Win32.py文件内已经预设好截图并保存文件代码
        (!)制作模板图像的时候都以 CV处理图像分辨率(默认1280x720) 为主
           定义模板对象时的 ROI区域、反馈区域 也以CV处理图像分辨率为主
           匹配结果、反馈区域的坐标 会利用cvScale转换为安卓触屏的实际坐标

     1.1 修改*Win32.py脚本 
        (1)if __name__ == '__main__' : 内的 VM = GetVMScreen(title='VM')
           title='VM' 的 VM 改为目标模拟器的窗口标题，可在任务管理器里看到这个标题
        (2)save = 'debug\\' + time.strftime('%Y%m%d.%H%M%S', time.localtime(time.time()))[2 :] + '.tif'
           'debug\\' 的 debug 为保存截图的文件夹，可以修改，若不存在需要自行建立
        (3)执行*Win32.py脚本后，若修改正确会在保存文件就里看到一个以时间格式为文件名的tif图像文件

     1.2 裁剪被识别图像模板
        (0)本教程以Photoshop为主，且不会过多强调在PS里如何操作
           也可以使用其他支持 选区 图层 辅助线 快速导出图层 的二维图像编辑工具
        (1)使用选区尽可能大的选定 被识别图像区域，
           (不要包含其他无关内容，除非没办法了或使用透明图像匹配)
           例如要选找 [圆角的确定按钮]，就矩形选择 [圆角的确定按钮] 但不包含左右两边的圆角部分
        (2)然后Ctrl+J拷贝图层，会得到一个新图层，双击它的文字重命名为方便后期寻找的名字
           (若需要透明匹配，给指定模板图层加蒙版，然后使用铅笔黑色画掉希望透明的区域)
           例如 01某界面01某按钮，可以让资源管理器按照前面的数字顺序排列显示文件
        (3)然后选定背景图层，选下一个模板再Ctrl+J拷贝图层得到所有需要的图像模板
           (不选背景图层就Ctrl+J空气了，PS会报错区域为空)
        (4)重复123到所有希望使用的模板都选完
        (5)最后按住Ctrl选择所有模板图层，右键快速导出为PNG，在保存的文件夹可以看到导出的图像
        (6)保存tif文件，方便以后修改，默认设置的tif会记住图层
          
     1.3 在脚本里定义模板
        (0)定义模板的目的是在一个对象里保存模板的图像、感兴趣区域、模拟触摸区域、注释信息、文件读取模式等
        (1)使用definetl(图像文件集根目录, 图像文件路径, 文本注释, 感兴趣区域, 反馈触摸区域, [读取模式])
            definetl('.\\AAAA\\', 'Image.png', 'xxxxx', ...)
        (2)读取模式支持 definetl.RGBA definetl.RGB definetl.Gray 必须套一层[]传参
            definetl(... ,[definetl.RGBA])
        (3)感兴趣区域为元组(X1,Y1,X2,Y2)仅绝对区域，预设支持*public.py内 roiFull(匹配0，0到1280,720全图)
            definetl(... , (0, 0, 1280, 720), (0, 0, 1280, 720), ...)
            definetl(... , roiFull, (0, 0, 1280, 720), ...)
        (!)相对区域使用*public.py内cal(pos0, mv1, mv2, mv3, mv4)函数，其中pos0为*public.py内mo(Enum)枚举，
            传入pos0=mo.SELF可配置为：匹配成功的坐标为原点，经过mv1,mv2移动后，大小为宽mv3高mv4的区域
            传入mo.LT则是图像左上角(Left-Top)为原点，mo.RB则是图像右下角(Right-Bottom)为原点
            更多pos0参数查找本项目的mo枚举类
        (4)反馈触摸区域为元组(X1,Y1,X2,Y2)可以为相对区域，预设支持*public.py内 fbNone(不点任何区域) fbSelf(点击自己)
            definetl(... , roiFull, cal(mo.SELF, -50, 90, 100, 90), ...) 
            definetl(... , roiFull, fbSelf, ...) 
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
             识别函数(... ,demo['中文:名字1'] , ...) # 传入模板类组，匹配第一个失败就匹配第二个，直到成功或全部失败
             识别函数(... ,demo['中文:名字1'][1] , ...) # 传入模板类组的第二个模板类
             识别函数(... ,demo['中文:名字2'] , ...) # 传入模板类
             
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
           使用*public.py内GetFBXY(xy,tl)函数，xy为元组(x,y)
           tl可以为模板类对象，或元组(x1,x2,y1,y2)，或*public.py内cal()的返回值
           例如 XY = GetFBXY(XY, tl=tl)
           使用随机可降低被反作弊或机器人检测发现的概率

#### 2.基本功能函数

     2.0 基本逻辑
         识别(按钮) → 成功该干什么(点击按钮) → 干了有什么现象(按钮消失或某东西出现) → 完成
         使用有反馈的逻辑，就算模拟器卡顿了，但在超时前响应完成，可以优化脚本的逻辑反应速度

     2.1 图像识别
         在*.MATCH.py里提供了三个函数封装和一个枚举
            mt(Enum) 匹配函数功能开关，套[]传入param，详细开关查找本项目的mt枚举类
            mask(screen, tlclass, threshold=0.8, param=None) 透明匹配函数
            rect(screen, tlclass, threshold=0.8, param=None) 矩形匹配函数
            matchtl(screen, tlclass, threshold=0.8, param=None) 自动匹配函数，自动选择mask()或rect()

         screen 为被识别背景
         tlclass 为模板类列表或模板类
         threshold 为识别成功阈值
         param 为功能开关(例如 mt.rgb为彩色识别(默认灰度)，可以使用列表同时传入多个开关，如果函数不支持会直接舍弃)
         
         例如 xy = matchtl(mu.GetScreen(), tl, threshold, [mt.quiet]) # 为静默不输出日志匹配
         其中 matchtl() 支持 模板类列表 输入 和 直接模板类 输入，mask()与rect()只支持直接模板类输入无法遍历列表

         
     2.2 虚拟触摸
         在*android.py里提供一个类用于定义安卓模拟器设备，且应该在脚本主循环运行之前执行
             mudevice(addr="IP:Port", title="xxxx")
         参数 addr 是模拟器ADB网络IP地址端口，title 为模拟器实例窗口标题，inputdev 为触摸设备事件地址
         使用 mudevice.inputTouch(xy, endSleep=退出等待float秒数) 方法进行虚拟触摸

#### 3.死循环控制系统

     3.0 块作用域
         复杂匹配逻辑就需要路由系统指导死循环时执行哪一段代码
         例如 while True : 
                while flag==1 : ...
                while flag==2 : ...
                while flag==3 : ...
         其中1 2 3对应的是不同的阶段，该使用什么识别组合，关闭不必要的算法提高脚本的实时性
         以及防止相似场景的错误匹配成功，例如两个场景都有一样的确认按钮，但功能完全不同甚至相反
         
     3.1 根作用域检测
         根作用域指的是作用域集合，
         (例如 1-1 1-2 1-3 1-4 都是 1- 开头，只允许 1-X 通过)
         该操作可以保证进入正确的死循环，
         (例如 1-1 进入 2-X，但检测发现 1-1 不是 2- 开头，就会无法死循环马上执行后面代码)
         本项目提供了作用域标志类对象
             class FlagInit(flagNum, flagNote='L', base=0)
             flagNum -> 作用域序号，所属根作用域内唯一，范围 0 到 255 
             flagNote -> 作用域注释，用于显示执行位置时的字符串
             base -> 根作用域号，整个自定义脚本唯一，范围 0x00 到 0xFF
      
      3.2 作用域管理
          本项目提供了作用域管理类对象
              class FlagCtrl(flag)  # 创建对象时设定 flag 预设作用域
                  .get()            # 获取当前标志
                  .note()           # 获取当前标志的注释
                  .isBase(base)     # 判断当前标志是否属于传入base分类
                  .set(flag, param) # 改变当前标志并更新导航信息
                  .IS(flag)         # 判断当前标志是否等于传入flag
              其中 param 可传入控制符：
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
     *android.py 内提供了如下类与方法
     　  定义安卓模拟器 mudevice(addr=Adb控制IP地址端口, title=模拟器窗口标题, inputdev=触摸事件输入地址)
     　  连接设备 mudevice.connect()
         发送指令 mudevice.command(单行shell指令)
         发送事件 mudevice.sendevent(事件列表)
         调试触摸 mudevice.inputTouch(数组(x,y), 结束延迟)
         事件触摸 mudeviceandroidTouch(数组(x,y), 按压时间, 重复次数, 每次结束延迟)
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
     *public.py 内提供了如下类与方法
     　  定义资源 definetl(图像文件集根目录, 图像文件路径, 文本注释, 感兴趣区域, 反馈触摸区域, [读取模式])
                 例如 自定义脚本的资源存放于 AAAA文件夹下：definetl('.\\AAAA\\', 'Image.png', 'xxxxx', ....)
                 感兴趣区域与反馈触摸区域 元组(X1,Y1,X2,Y2) 是基于CV算法分辨率的像素区域
                 例如1280x720的算法分辨率，只对左上角100,100到200,200区域进行图像匹配：(100,100,200,200)
                 只对150,150到250,250区域内进行安卓模拟点击 (150,150,250,250)，实际使用需要缩放回模拟器的实际坐标
