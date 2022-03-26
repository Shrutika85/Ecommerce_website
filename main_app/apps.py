from django.apps import AppConfig


class AiModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'

import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    UPLOAD_FOLDER = os.getcwd() + '/app/static/img/'