# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-26 下午3:32

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
