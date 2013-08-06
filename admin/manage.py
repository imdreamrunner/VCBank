from datetime import datetime
import web
from models import *
import json
from web.contrib.template import render_jinja

view = render_jinja('view/admin')

class index:
    def GET(self):
        inputs = web.input()
        if 'frame' in inputs:
            try:
                frame = getattr(view, inputs.frame)
                return frame()
            except BaseException:
                return 'Unable to load frame ' + inputs.frame
        else:
            return view.index()

class display:
    def GET(self):
        inputs = web.input()
        if not 'm' in inputs:
            return 'Model not specified'
        m = inputs.m
        if m == 'account':
            user = User.getOne(inputs.uid)
            create_time = datetime.fromtimestamp(user.create_time).strftime('%Y-%m-%d %H:%M:%S')
            user['create_time_string'] = create_time
            return view.displayAccount(user = user)

class getData:
    def GET(self):
        return "Undefined method"

    def POST(self):
        inputs = web.input()
        if inputs.request == 'users':
            order = where = False
            if 'order' in inputs:
                order = inputs.order
            if 'where' in inputs:
                where = inputs.where
            if order and where:
                users = User.getAllSafely(order, where)
            elif order:
                users = User.getAllSafely(order)
            elif where:
                users = User.getAllSafely(where = where)
            else:
                users = User.getAllSafely()
            return json.dumps(users)