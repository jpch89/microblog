# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-27 上午10:21

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length

from app.models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField('密码', validators=[DataRequired(message='密码不能为空')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired('用户名不能为空')])
    email = StringField('电子邮箱', validators=[DataRequired('电子邮箱不能为空'), Email()])
    password = PasswordField('密码', validators=[DataRequired('密码不能为空')])
    password2 = PasswordField('重复输入密码',
                              validators=[DataRequired('密码不能为空'), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('请使用其它的用户名')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('邮箱地址已存在，请使用其它电子邮箱。')

class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    about_me = TextAreaField('关于我', validators=[Length(min=0, max=140)])
    submit = SubmitField('提交')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('用户名已存在，请输入其它用户名。')


class PostForm(FlaskForm):
    post = TextAreaField('写点什么', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('提交')
