#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding:utf-8
import sys

from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
import subprocess

# 初始化



device = MonkeyRunner.waitForConnection(10.0,"127.0.0.1:21503")

easyDevice = EasyMonkeyDevice(device)

for i in range(0,100):

	# 点击列表评论区域

	easyDevice.touch(By.id('id/comment_cnt'),MonkeyDevice.DOWN_AND_UP)

	MonkeyRunner.sleep(4)

	# 点击内容评论区域

	easyDevice.touch(By.id('id/comment_ll'),MonkeyDevice.DOWN_AND_UP)

	MonkeyRunner.sleep(4)

	# 输入评论

	string = "adb shell am broadcast -a ADB_INPUT_TEXT --es msg "+u"看起来很漂亮"+str(randint(0,1000))

	subprocess.check_call(string)

	MonkeyRunner.sleep(4)

	# 点击发布评论

	easyDevice.touch(By.id('id/confirm'),MonkeyDevice.DOWN_AND_UP)

	MonkeyRunner.sleep(2)

	# 检查是否发布失败，失败就叉掉

	if True == easyDevice.visible(By.id('id/close')):
		
		# 失败了

		easyDevice.touch(By.id('id/close'),MonkeyDevice.DOWN_AND_UP)
		
		MonkeyRunner.sleep(4)

		easyDevice.touch(By.id('id/button1'),MonkeyDevice.DOWN_AND_UP)
		
		MonkeyRunner.sleep(4)

	# 点击返回

	easyDevice.touch(By.id('id/top_left'),MonkeyDevice.DOWN_AND_UP)

	MonkeyRunner.sleep(2)

	# 下滑

	device.drag((200,500+919),(200,500),5,5)


	