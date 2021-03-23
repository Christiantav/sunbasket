import os
from flask import Flask
from .models import db
from .config import *
# from flask_sqlalchemy import SQLAlchemy
import logging

def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://candidate:ur8EHudXjAVW#2rG@interview.sunbasket-dev.com:3306/sunbasket'
  # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://candidate:ur8EHudXjAVW#2rG@interview.sunbasket-dev.com:3306/sunbasket'
  app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
  logging.basicConfig(level=logging.DEBUG)
  app.logger.info("Starting Sunbasket")
  db.init_app(app)

  return app
