# 连接手机

```
from com.android.monkeyrunner import MonkeyRunner
device = MonkeyRunner.waitForConnection()
```

注释：等待连接设备，与模拟器链接，返回monkeydevice对象，代表链接的设备。没有报错的话说明连接成功。
参数：timeout：超时时间，单位秒，浮点数。默认是无限期等待。
          deviceId：指定的设备名称。默认为当前的设备（手机有限，比如手机通过usb线链接到pc、其次为模拟器）。
实例：默认连接：device=MonkeyRunner.waitForConnection()
           参数连接：device=mr.waitForConnection(1.0,'emulator-5554')

# 部分按键操作
```
device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
device.touch(100,100,MonkeyDevice.DOWN_AND_UP)
```
注释：类似上面这种，press()操作和touch()操作
参数：press的第一个参数是keyevent，这个可以在https://developer.android.com/reference/android/view/KeyEvent中查找
	 /*
	 menu键：KEYCODE_MENU
	home键：KEYCODE_HOME
	back键：KEYCODE_BACK
	search键：KEYCODE_SEARCH
	call键：KEYCODE_CALL
	end键：KEYCODE_ENDCALL
	上音量键：KEYCODE_VOLUME_UP
	下音量键：KEYCODE_VOLUME_DOWN
	power键：KEYCODE_POWER
	camera键：KEYCODE_CAMERA
	 */
	 press的第二个参数是操作类型，有三种MonkeyDevice.DOWN，MonkeyDevice.DOWN_AND_UP， MonkeyDevice.UP
	 对于touch也是一样，不过touch的第一个参数是触摸的X点，第二个参数是触摸的Y点

```
device.drag((100,100),(200,200),1000,5)
```
drag操作就是滑动，第一个是开始的坐标，第二个是截止的坐标，第三个是持续时间，第四个是这个过程的力度
drag貌似是唯一一个实现长按的方法

# 安装软件包

```
from com.android.monkeyrunner import MonkeyRunner
device.installPackage('myproject/bin/MyApplication.apk') 
```
注释： #参数是相对或绝对APK路径 路径级别用“/”，不能用“\”
参数：path：被安装到设备上的apk包在电脑上的文件路径
实例：device.installPackage('myproject/bin/MyApplication.apk') 

# 删除软件包

```
device.removePackage('myproject/bin/MyApplication.apk')
```

# 启动app（activity）

```
from com.android.monkeyrunner import MonkeyRunner
device.startActivity(component="your.www.com/your.www.com.TestActivity") 
```
注释：启动任意的Activity，此时可以向模拟器发送如按键、滚动、截图、存储等操作了。 执行一个adb shell命令，并返回结果，如果有的话
device.shell("...")
参数：uri - The URI for the Intent.
           action - The action for the Intent.
           data - The data URI for the Intent
           mimetype - The mime type for the Intent.
           categories - A Python iterable containing the category names for the Intent.
           extras - A dictionary of extras to add to the Intent. Types of these extras are inferred from the python types of the values.
           component - The component of the Intent.
           flags - An iterable of flags for the Intent.All arguments are optional. The default value for each argument is null.
实例：device.startActivity(component="your.www.com/your.www.com.TestActivity") 
           device.startActivity(component="your.www.com/.TestActivity") 

# 输入字符

```
from com.android.monkeyrunner import MonkeyRunner
device.type（‘字符串’）
```
注释：键盘上的类型指定字符串，这相当于要求字符中按（键码，DOWN_AND_UP）字符串发送到键盘
参数：message：要键入的字符串
实例：device.type（‘字符串’）

# 唤醒设备

```
device.wake()
```

# 重启

```
device.reboot()
```

# 获取一些系统参数

就两个方法，getProperty()和getSystemProperty()，这两个需要查询的参数都可以通过adb shell getprop获取到

# 运行设备指定的包

```
device.instrument(String className, dictionary args)
```
这个方法基本上就是用于处理包名重复的问题
