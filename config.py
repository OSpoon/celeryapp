#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-18 14:24
# @Author : Spoon
# @Site : 
# @File : config.py
# @Software: PyCharm
from datetime import timedelta

from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    'app.task1',
    'app.task2',
)

CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'app.task1.sendMsg',
        'schedule': timedelta(seconds=6),
        'args': ('定时早上好',)
    },
    'task2': {
        'task': 'app.task2.sendMsg',
        'schedule': crontab(hour=23, minute=15),
        'args': ('定时晚上好',)
    }
}