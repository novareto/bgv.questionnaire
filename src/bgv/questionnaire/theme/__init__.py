from reiter.ui import TemplateLoader
from fanstatic import Library, Resource, Group
from roughrider.application.request import Request
from reiter.ui.registry import UIRegistry


TEMPLATES = TemplateLoader("./templates")
library = Library("bgv.questionnaire", "./static")
custom_css = Resource(library, "custom.css")


bootstrap_css = Resource(
    library,
    "uvc_serviceportal_bootstrap.css",
    compiler="sass",
    source="scss/siguv.scss",
)


bootstrap_js = Resource(
    library,
    "bootstrap-5.1.3/dist/js/bootstrap.bundle.min.js",
    bottom=True
)


def theme(name):
    return type(name, (UIRegistry,), {})(
        macros=TEMPLATES['macros.pt'].macros, templates=TEMPLATES,
        resources=[custom_css, bootstrap_css, bootstrap_js]
    )
