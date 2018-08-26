# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-26 下午3:33

# 第一个 app 是 app 包，是文件夹
# 第二个 app 是 app 变量，是 Flask 核心对象
from app import app


@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'
