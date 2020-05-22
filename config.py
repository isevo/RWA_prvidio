import os
import sqlite3
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'moj_jako_jako_tajni_kljuc')
    ADMIN_KEY = os.getenv('ADMIN_KEY', 'ja_sam_admin')
    RESTPLUS_MASK_HEADER = False
    RESTPLUS_MASK_SWAGGER = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
   # SQLALCHEMY_DATABASE_URI = 'sqlite:///todo_dev.db'
   # SQLALCHEMY_DATABASE_URI = 'sqlite:///meal.db'
   
    SQLALCHEMY_TRACK_MODIFICATIONS = False


secret_key = Config.SECRET_KEY
