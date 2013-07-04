import web
from models import *
from web.contrib.template import render_jinja

view = render_jinja('view/visitor')

class index:
    def GET(self):
        return view.index(user = User.status())

class earn:
    def GET(self):
        return view.earn(user = User.status())

class donate:
    def GET(self):
        return view.donate(user = User.status())
