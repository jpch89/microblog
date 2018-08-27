# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-27 上午10:21

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')
