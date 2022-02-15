import wtforms
import horseman.response
from reiter.form import trigger
from reiter.ui.components import FormPage
from bgv.questionnaire.application import app, backend
from bgv.questionnaire.browser import TEMPLATES
from bgv.questionnaire.theme import GLOBAL_MACROS


class Login(wtforms.Form):

    username = wtforms.StringField(
        'Benutzername',
        description="E-Mail Adresse oder Aktenzeichen",
        validators=[wtforms.validators.InputRequired()]
    )

    password = wtforms.PasswordField(
        'Passwort',
        validators=[wtforms.validators.InputRequired()])


@app.routes.register('/login')
@backend.routes.register('/login')
class LoginForm(FormPage):

    title = "Anmelden"
    description = "Bitte tragen Sie hier Ihre Anmeldeinformationen ein"
    base_template = TEMPLATES['form.pt']

    @property
    def namespace(self):
        ns = super(LoginForm, self).namespace
        ns['macros'] = GLOBAL_MACROS
        return ns

    @property
    def action(self):
        return self.request.environ["SCRIPT_NAME"] + "/login"

    def setupForm(self, data=None, formdata=None):
        form = Login()
        form.process(data=data, formdata=formdata)
        return form

    @trigger("Anmelden", order=1, css="btn btn-primary")
    def login(self, data):
        form = self.setupForm(formdata=data.form)
        if not form.validate():
            return {"form": form}
        auth = self.request.app.utilities['authentication']
        if (user := auth.from_credentials(self.request.environ, form.data)) is not None:
            auth.remember(self.request.environ, user)
            return self.redirect(self.request.environ["SCRIPT_NAME"] + "/")

        return self.redirect(self.request.environ["SCRIPT_NAME"] + "/")

    @trigger("Abbrechen", css="btn btn-secondary")
    def cancel(form, *args):
        pass
