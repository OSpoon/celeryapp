#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-18 14:24
# @Author : Spoon
# @Site : 
# @File : task1.py
# @Software: PyCharm
import time

from app import celery_app


@celery_app.task
def sendMsg(msg):
    time.sleep(3)
    print('task1 : ', msg)
