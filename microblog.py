# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-26 下午4:02

from app import app, db
from app.models import User, Post
from app import cli

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

