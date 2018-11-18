from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask('sayhello')
app.config.from_pyfile('setting.py')

# 消除 jinja2 無意義的空行
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

from sayhello import views, errors, commands