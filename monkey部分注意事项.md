逍遥模拟器注意事项：

1.adb devices执行之后自动断开：

解决方法：
关闭逍遥安卓模拟器
关闭adb所有进程
将android-sdk-windows/bin目录下的adb.exe拷贝到逍遥模拟器安装目录下（先删除原有的adb.exe）
重启逍遥安卓模拟器，点击设置，点击 关于平板电脑 连续点击 android版本 6次
使用 adb devices 就可以找到模拟的系统了

2.monkeyruuner报错问题

解决方法：
为了防止错误，存了一份放到了github上面
之后使用的时候，要安装了androidstudio，借助这个里面的sdk来使用，或者下载一份完整的build/tools

3.windows环境下解码出现lookuperror问题：

解决方法：
在命令行中运行chcp 437切换一下即可

4.viewserver启动

viewserver需要在可以root的手机上面才有可能启动。
切记执行命令之前先remount一下

检查是否启动：adb shell service call window 3 返回值为Result: Parcel(00000000 00000000 '........')"为未启动

打开viewserver方法：adb shell service call window 1 i32 4939
关闭viewserver方法：adb shell service call window 2 i32 4939

5.处理unicode问题

text.encode('utf-8')

6.adb端口问题

ADB是服务通过扫描奇数端口5555 至5585查找  Android模拟器或设备。而且每个设备占用2个端口，偶数端口Android设备控制台，奇数端口Android与ADB的连接。

7.adb无法输入中文问题

安装adbkeyboard即可