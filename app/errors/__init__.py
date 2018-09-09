# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-9-8 下午4:57

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
