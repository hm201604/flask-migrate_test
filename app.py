from flask import Flask
from ext import db
import config
#目的：练习Flask-Migrate模块的使用
#安装依赖：  pip install flask-migrate
#其他依赖：
            #pip install pymysql
            #pip install SQLAlchemy
            #pip install flask-sqlalchemy
            #pip install flask-script
 
#迁移命令
# 1.python manage.py db init
# 2.python manage.py db migrate
# 3.python manage.py db upgrade
 
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)      #载入config.py中的配置信息
 
    db.init_app(app)  # app绑定数据库db
 
    return app
 
if __name__ == '__main__':
    app = create_app()
    app.run()
