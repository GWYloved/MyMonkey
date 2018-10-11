# 截图

```
from com.android.monkeyrunner import MonkeyRunner,MonkeyImage
result = device.takeSnapshot()
```
注释：获取设备的屏蔽缓冲区，产生了整个显示器的屏蔽捕获。（截图）
参数：无
实例：result=device.takeSnapshot()
    返回一个MonkeyImage对象（点阵图包装），我们可以用一下命令将图保存到文件
    result.writeToFile('takeSnapshot\\result1.png','png')

# 保存到文件

```
from com.android.monkeyrunner import MonkeyRunner,MonkeyImage
result = device.takeSnapshot()
result.writeToFile('takeSnapshot\\result1.png','png')
```
注释：将截图保存到文件 写成功返回true，否则返回false
参数：path：输出文件名和路径
          format：目标格式
实例：result.writeToFile('takeSnapshot\\result1.png','png')

# 将图片转为字节码

```
result.convertToBytes(String format)
```
将图片转为字节码，参数是格式，默认是转为png

# 获取指定地点的像素

```
result.getRawPixel(integer x, integer y)
```
以argb数组的形式返回指定地点的像素

```
result.getRawPixelInt(integer x, integer y)
```
以int的形式返回部分的颜色

# 截取图像

```
cutResult = result.getSubImage(tuple rect)
```
截取图像中的长方形区域，并生成新的图

# 判断两个图片的相似度

```
boolean sameAs(MonkeyImage otherImage, float percent)
```
参数1为需要对比的图片，参数2为相似程度，原理为对比像素