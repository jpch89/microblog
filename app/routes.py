# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-26 下午3:33

from flask import render_template
# 第一个 app 是 app 包，是文件夹
# 第二个 app 是 app 变量，是 Flask 核心对象
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': '进击的团子'}
    posts = [
        {
            'author': {'username': '路飞'},
            'body': '今天要去救山治！'
        },
        {
            'author': {'username': '乔巴'},
            'body': '集市的棉花糖好好吃！'
        }
    ]
    return render_template('index.html', title='首页', user=user, posts=posts)
    # return render_template('index.html', user=user)
