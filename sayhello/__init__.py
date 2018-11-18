from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_moment import Moment

app = Flask('sayhello')
app.config.from_pyfile('setting.py')

# 消除 jinja2 無意義的空行
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
moment = Moment(app)

from sayhello import views, errors, commands