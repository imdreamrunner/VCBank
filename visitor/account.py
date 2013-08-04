import web
import json
import core

from models import *
from web.contrib.template import render_jinja

view = render_jinja('view/visitor')

class create:
    def GET(self):
        return view.signup(user = User.status())

    def POST(self):
        """
        @return: json(@error)
        """
        try:
            User.create(dict(web.input()))
            return json.dumps({'error': 0})
        except AttributeError:
            # Missing information
            return json.dumps({'error': 1})
        except Exception as exception:
            errorCode =  int(exception.message)
            if errorCode > 1:
                return json.dumps({'error': errorCode})
            else:
                # Unknown error
                return json.dumps({'error': 9999})

class login:
    def GET(self):
        return view.login(user = User.status())

    def POST(self):
        try:
            inputs = web.input()
            User.login(inputs.email, inputs.password)
            return json.dumps({'error': 0})
        except AttributeError:
            # Missing information
            return json.dumps({'error': 1})
        except Exception as exception:
            errorCode =  int(exception.message)
            if errorCode > 1:
                return json.dumps({'error': errorCode})
            else:
                # Unknown error
                return json.dumps({'error': 9999})

class display:
    def GET(self):
        status = User.status()
        if status:
            return view.account(user = status)
        else:
            return -1

class logout:
    def GET(self):
        if 'uid' in core.session:
            del core.session.uid
        raise web.seeother('/login')