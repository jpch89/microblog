# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-8 下午5:04

from flask import render_template, current_app
from flask_babel import _
from app.email import send_mail


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail(_('[微博客]重置密码'),
              sender=current_app.config['ADMINS'][0],
              recipients=[user.email],
              text_body=render_template('email/reset_password.txt',
                                        user=user, token=token),
              html_body=render_template('email/reset_password.html',
                                        user=user, token=token))
