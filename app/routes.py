# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-26 下午3:33

from flask import render_template, flash, redirect, url_for
# 第一个 app 是 app 包，是文件夹
# 第二个 app 是 app 变量，是 Flask 核心对象
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('登录请求来自用户 {} ，记住我={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='登录', form=form)
