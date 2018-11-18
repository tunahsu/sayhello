import os
import sys
from sayhello import app

SECRET_KEY = os.getenv('SECRET_KEY', 'fucking secret')

# sqlite URI 兼容
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

# 若設置為 True 則 Flask-SQLAlchemy 會自動追蹤被修改的物件
# 需要額外記憶體，不必要可以禁用
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)