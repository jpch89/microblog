# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-26 下午10:55

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
