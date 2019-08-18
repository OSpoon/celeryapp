#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-18 14:25
# @Author : Spoon
# @Site : 
# @File : task2.py
# @Software: PyCharm
import time

from app import celery_app


@celery_app.task
def sendMsg(msg):
    time.sleep(5)
    print('task2 : ',msg)