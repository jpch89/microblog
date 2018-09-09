# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-26 下午4:02

from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
