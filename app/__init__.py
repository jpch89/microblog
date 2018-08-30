# -*- coding: utf-8 -*-
# @Author: jpch89
# @Time:   18-8-26 下午3:32

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# models 用来定义数据库的模型
from app import routes, models
