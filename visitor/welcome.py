import web

view = web.template.render('view/welcome')

class index:
    def GET(self):
        return view.index()

class earn:
    def GET(self):
        return view.earn()

class donate:
    def GET(self):
        return view.donate()
