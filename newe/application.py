from gevent import monkey
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from config import config


class Application(Flask):
    def __init__(self, import_name):
        template_folder = os.getcwd() + '/web/templates'
        static_folder = os.getcwd() + '/web/static'

        # config = os.path.join(path,'config/config.py')
        super().__init__(import_name=import_name, template_folder=template_folder, static_folder=static_folder)
        self.config.from_object(config)
#         db.init_app(self)
#
#
# db = SQLAlchemy()
app = Application(__name__)
app.secret_key = os.urandom(24)
if app.config['RUN_ENVIRON'] != 'local':
    monkey.patch_all()

from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
