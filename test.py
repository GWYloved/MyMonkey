#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

device = MonkeyRunner.waitForConnection()

device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)

# selectString = MonkeyRunner.alert(u"我日",u"riri",u"jeje")

# selectString = MonkeyRunner.choice("choice a sex", ["man", "woman"], "rorororor")

# print type(selectString)

# print selectString

# selectString = "press"+ selectString

# MonkeyRunner.alert(selectString,u"确认",u"确认")

# MonkeyRunner.help("text")

inputString = MonkeyRunner.input("message","initialvalue","title","oktitle","canceltitle")

print inputString.decode("utf-8")