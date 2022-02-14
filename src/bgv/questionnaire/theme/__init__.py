from reiter.ui import TemplateLoader
from fanstatic import Library, Resource, Group
from roughrider.application.request import Request
from bgv.questionnaire.application import app


TEMPLATES = TemplateLoader("./templates")
GLOBAL_MACROS = TEMPLATES['macros.pt'].macros


library = Library("bgv.questionnaire", "./static")
custom_css = Resource(library, "custom.css")


@app.ui.register_layout(app.request_factory)
class Layout:

    _template = TEMPLATES["layout.pt"]

    def __init__(self, request, name):
        self.name = name

    def title(self, view):
        return getattr(view, 'title', 'UVCReha')

    def render(self, content, **namespace):
        theme.need()
        return self._template.render(
            layout=self, content=content, **namespace)


@app.ui.register_slot(name="sitecap")
def sitecap(request, name, view, context):
    return TEMPLATES["sitecap.pt"].render(request=request)


@app.ui.register_slot(name="globalmenu")
def globalmenu(request, name, view, context):
    actions = list(
        request.app.get_actions(request, classifiers=('global',)))
    return TEMPLATES["globalmenu.pt"].render(request=request, actions=actions)


@app.ui.register_slot(name="messages")
def messages(request, name, view, context):
    utility = request.utilities.get("flash")
    if utility is None:
        return ""
    return TEMPLATES["messages.pt"].render(messages=list(utility))


@app.ui.register_slot(name="footer")
def footer(request, name, view, context):
    return TEMPLATES["footer.pt"].render(request=request)
