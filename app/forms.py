# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-27 上午10:21

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
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


class EditProfileForm(FlaskForm):
    username = StringField(_l('用户名'), validators=[DataRequired()])
    about_me = TextAreaField(_l('关于我'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('提交'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError(_('用户名已存在，请输入其它用户名。'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('写点什么'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('提交'))
