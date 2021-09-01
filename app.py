from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from exts import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
from models import Post
db.init_app(app)
migrate = Migrate(app, db)