# Helper 
     一个使用Python编写，基于OpenCV的画面内容识别算法项目
     该项目还处于初级开发阶段，任何功能函数方法都具有不确定的变更，但会尽可能的不变更函数调用方式
     
### 警告 该项目几乎违反所有网络游戏或网络软件的用户协议!
     仅允许个人以学习为目的使用 禁止用于任何商用盈利违法等用途
     因使用本项目 产生的一切问题后果由使用者自行承担 产生的任何法律后果由使用者自行承担
     
     后果包括但不限于：游戏封禁或回档、账户拉黑或锁定、违法相关法律法规被起诉
 
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
