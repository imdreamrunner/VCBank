import web
from models import *
from web.contrib.template import render_jinja

view = render_jinja('view/admin')

class index:
    def GET(self):
        return view.index()

class dashboard:
    def GET(self):
        return view.dashboard()