#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-18 14:30
# @Author : Spoon
# @Site : 
# @File : run.py
# @Software: PyCharm

from app.task1 import sendMsg as sendTask1Msg
from app.task2 import sendMsg as sendTask2Msg

sendTask1Msg.delay('早上好')
sendTask2Msg.delay('晚上好')