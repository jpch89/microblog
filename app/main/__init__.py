# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-8 下午5:31

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes
