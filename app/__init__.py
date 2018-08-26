# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-26 下午3:32

from flask import Flask

app = Flask(__name__)

from app import routes
