"""import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True"""
from app import db, Project
db.create_all()
sample=Project('crazy', 'need amazing skills', "AI", "12-3-60", 1200, "qwe")
db.session.add(sample)
db.session.commit()
projects=Project.query.filter_by(project_name="crazy")
for pro in projects:
    print(pro.id)