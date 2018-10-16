#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding:utf-8
import sys

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
import subprocess

device = MonkeyRunner.waitForConnection(10.0,"127.0.0.1:21503")

easyDevice = EasyMonkeyDevice(device)

if True == easyDevice.visible(By.id('id/button1')):

	print "find"

easyDevice.touch(By.id('id/button2'),MonkeyDevice.DOWN_AND_UP)

print easyDevice.locate(By.id('id/button2'))
		
MonkeyRunner.sleep(2)