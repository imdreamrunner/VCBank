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

class accounts:
    def GET(self):
        return view.accounts()

class accountsSearch:
    def GET(self):
        return view.accountsSearch()

class accountsLists:
    def GET(self):
        return view.accountsLists()

class getAccounts:
    def GET(self):
        return True