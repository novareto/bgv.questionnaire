from reiter.ui import TemplateLoader
from roughrider.application.request import Request
from bgv.questionnaire.application import app, backend


TEMPLATES = TemplateLoader("./layout")


@app.ui.register_layout(app.request_factory)
@backend.ui.register_layout(backend.request_factory)
class Layout:

    _template = TEMPLATES["layout.pt"]

    def __init__(self, request, name):
        self.name = name

    def title(self, view):
        return getattr(view, 'title', 'UVCReha')

    def render(self, content, **namespace):
        return self._template.render(
            layout=self, content=content, **namespace)


@app.ui.register_slot(app.request_factory, name="sitecap")
@backend.ui.register_slot(backend.request_factory, name="sitecap")
def sitecap(request, name, view, context):
    return TEMPLATES["sitecap.pt"].render(request=request)


@app.ui.register_slot(app.request_factory, name="globalmenu")
@backend.ui.register_slot(backend.request_factory, name="globalmenu")
def globalmenu(request, name, view, context):
    actions = list(
        request.app.get_actions(request, classifiers=('global',)))
    return TEMPLATES["globalmenu.pt"].render(
        request=request, actions=actions)


@app.ui.register_slot(app.request_factory, name="messages")
@backend.ui.register_slot(backend.request_factory, name="messages")
def messages(request, name, view, context):
    utility = getattr(request, 'flash', None)
    if utility is None:
        return ""
    return TEMPLATES["messages.pt"].render(messages=list(utility))


@app.ui.register_slot(app.request_factory, name="footer")
@backend.ui.register_slot(backend.request_factory, name="footer")
def footer(request, name, view, context):
    return TEMPLATES["footer.pt"].render(request=request)
