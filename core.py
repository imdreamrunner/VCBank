import web
import os

web.config.debug = False

def run(urls):
    global app, db, session
    db = web.database(dbn='mysql', user='vcbank', pw='vcbank', db='vcbank')
    app = web.application(urls, globals())
    currentDir = os.path.dirname(__file__)
    session = web.session.Session(app, web.session.DiskStore(os.path.join(currentDir,'sessions')))

    app.run()