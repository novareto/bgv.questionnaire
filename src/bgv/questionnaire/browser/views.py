from reiter.ui.components import Page
from bgv.questionnaire.browser import TEMPLATES
from bgv.questionnaire.application import app


@app.routes.register('/')
class Index(Page):
    template = TEMPLATES['index']

    def GET(self):
        return {}


@app.routes.register('/favicon.ico')
class Index(Page):

    def GET(self):
        return ""
