#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

device = MonkeyRunner.waitForConnection()

device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)

MonkeyRunner.alert(u"我日",u"riri",u"jeje")