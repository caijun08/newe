from application import app

from web.controllers.newe import route_newe
from web.interrupt.interrupt import *
app.register_blueprint(route_newe, url_prefix='/newe')