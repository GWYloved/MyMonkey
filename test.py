#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

device = MonkeyRunner.waitForConnection()

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

if not easyDevice.visible(By.id('id/iftbl_Title')):
    raise Error('Could not find the "all apps" button')

print "Location of element:", easy_device.locate(By.id('id/iftbl_Title'))