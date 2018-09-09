# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-8 下午5:03

from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes
