import web
import utils.captcha
from models import *
from web.contrib.template import render_jinja

view = render_jinja('view/admin')

class login:
    def GET(self):
        return view.login()

class captcha:
    def GET(self):
        web.header("Content-Type", "image/png")
        captcha = utils.captcha.getCaptcha()
        # session.captcha = captcha[0]
        return captcha[1].read()