from reiter.ui.components import Page
from bgv.questionnaire.browser import TEMPLATES
from bgv.questionnaire.application import app, backend


@app.routes.register('/')
class Index(Page):
    template = TEMPLATES['index']

    def GET(self):
        return {}


@app.routes.register('/favicon.ico')
class Favico(Page):

    def GET(self):
        return ""


@backend.routes.register('/')
class AdminIndex(Page):

    def GET(self):
        return "admin"
