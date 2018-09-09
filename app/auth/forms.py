# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-8 下午5:04

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_l('用户名'), validators=[DataRequired(_l('用户名不能为空'))])
    password = PasswordField(_l('密码'), validators=[DataRequired(message=_l('密码不能为空'))])
    remember_me = BooleanField(_l('记住我'))
    submit = SubmitField(_l('登录'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('用户名'), validators=[DataRequired(_l('用户名不能为空'))])
    email = StringField(_l('电子邮箱'), validators=[DataRequired(_l('电子邮箱不能为空')), Email()])
    password = PasswordField(_l('密码'), validators=[DataRequired(_l('密码不能为空'))])
    password2 = PasswordField(_l('重复输入密码'),
                              validators=[DataRequired(_l('密码不能为空')), EqualTo('password')])
    submit = SubmitField(_l('注册'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('请使用其它的用户名'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('邮箱地址已存在，请使用其它电子邮箱。'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('电子邮箱'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('申请重置密码'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('密码'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('重复密码'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('立即重置密码'))

