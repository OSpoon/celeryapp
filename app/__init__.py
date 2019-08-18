#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-18 14:23
# @Author : Spoon
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
from celery import Celery

celery_app = Celery('celery_app')
celery_app.config_from_object('config')