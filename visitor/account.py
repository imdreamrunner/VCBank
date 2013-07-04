import web
import json
import core

from models import *

view = web.template.render('view/account')

class create:
    def GET(self):
        return view.create()

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
        return view.login()

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
        if 'user_id' in core.session:
            return view.display()
        else:
            return -1

class logout:
    def GET(self):
        if 'user_id' in core.session:
            del core.session.user_id
        raise web.seeother('/login')