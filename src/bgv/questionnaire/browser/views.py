from reiter.ui.components import Page
from reiter.ui.components import FormPage
from bgv.questionnaire.browser import TEMPLATES
from bgv.questionnaire.application import app, backend
from reiter.form import trigger
from wtforms_sqlalchemy.orm import model_form
from bgv.questionnaire.models import User
from bgv.questionnaire.browser import Form
from horseman.response import Response


@app.routes.register("/")
class Index(Page):
    template = TEMPLATES["index"]

    def GET(self):
        return {}


@app.routes.register("/favicon.ico")
class Favico(Page):
    def GET(self):
        return ""


@backend.routes.register("/")
class AdminIndex(Page):
    template = TEMPLATES["admin_index.pt"]

    def GET(self):
        session = self.request.environ["sql"]
        users = session.query(User).all()
        return dict(request=self.request, users=users)


@backend.routes.register("/add.user")
class AddUser(FormPage):
    template = TEMPLATES["admin_index.pt"]

    def setupForm(self, data=None, formdata=None):
        form = model_form(User, exclude=("answers"), base_class=Form)()
        form.process(data=data, formdata=formdata)
        return form

    @trigger("Speichern", order=1, css="btn btn-primary")
    def handle_save(self, data):
        form = self.setupForm(formdata=data.form)
        if not form.validate():
            return dict(form=form)
        data = data.form.to_dict()
        data = data.delete("form.trigger")
        session = self.request.environ["sql"]
        user = User(**data)
        session.add(user)
        return Response.redirect(self.request.application_uri)

    @trigger("Abbrechen", css="btn btn-secondary")
    def handle_cancel(self, data):
        return Response.redirect(self.application_uri)
