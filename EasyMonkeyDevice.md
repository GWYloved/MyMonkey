# 生成EasyMonkeyDevice

```
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice

device = MonkeyRunner.waitForConnection()

easyDevice = EasyMonkeyDevice(device)
```

# 点击触摸主窗口

```
easyDevice.touch(By selector, TouchPressType type)
```
示例：
```
easyDevice.touch(By.id('id/text1'),MonkeyDevice.DOWN_AND_UP)
```

# 根据id输入内容

```
easyDevice.type(By.id(noteId),'new')
```

# 判断控件是否存在

```
if True == easyDevice.exists(By.id(noteid)):
	print 'Note Exist'
```

# 判断控件是否显示

```
if True == easyDevice.visible(By.id(noteId)):
	print 'Note is Visible'
```

# 获取控件区域内容

```
text = easyDevice.getText(By.id(noteId))
```

# 获取聚焦的窗口id

```
focusId = easyDevice.getFocusedWindowId()
```

# 获取控件的位置

```
locate = easyDevice.locate(By.id(noteId))
```













