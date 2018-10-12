#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

device = MonkeyRunner.waitForConnection(10.0,"127.0.0.1:21503")

easyDevice = EasyMonkeyDevice(device)

# device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)

# id = By.id(ad_small_tab_ly)

# easyDevice.touch(id, )

# selectString = MonkeyRunner.alert(u"我日",u"riri",u"jeje")

# selectString = MonkeyRunner.choice("choice a sex", ["man", "woman"], "rorororor")

# print type(selectString)

# print selectString

# selectString = "press"+ selectString

# MonkeyRunner.alert(selectString,u"确认",u"确认")

# MonkeyRunner.help("text")

# inputString = MonkeyRunner.input("message","initialvalue","title","oktitle","canceltitle")

# print inputString.decode("utf-8")

# if not easyDevice.visible(By.id('id/comment_cnt')):
#     raise Error('Could not find the "comment_cnt" button')

# print "Location of element:", easyDevice.locate(By.id('id/comment_cnt'))

# easyDevice.touch(By.id('id/comment_cnt'),MonkeyDevice.DOWN_AND_UP)

# if not easyDevice.visible(By.id('id/comment_ll')):
#     raise Error('Could not find the "comment_ll" button')

# print "Location of element:", easyDevice.locate(By.id('id/comment_ll'))

# easyDevice.touch(By.id('id/comment_ll'),MonkeyDevice.DOWN_AND_UP)

# MonkeyRunner.sleep(1)

t = By.id('id/content')

if not easyDevice.visible(t):
    raise Error('Could not find the "content" button')

# print "Location of element:", easyDevice.locate(t)

# easyDevice.touch(By.id('id/content'),MonkeyDevice.DOWN_AND_UP)

# easyDevice.type(By.id('id/content'),'new')

device.type("hfdjahsdfkjahsf")

MonkeyRunner.sleep(1)

# if not easyDevice.visible(By.id('id/confirm')):
#     raise Error('Could not find the "confirm" button')

# print "Location of element:", easyDevice.locate(By.id('id/confirm'))

# easyDevice.touch(By.id('id/confirm'),MonkeyDevice.DOWN_AND_UP)