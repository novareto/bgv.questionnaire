from functools import partial
from dataclasses import dataclass, field
from reiter.ui.registry import UIRegistry
from reiter.view.utils import routables
from roughrider.routing.components import NamedRoutes
from roughrider.application import WrappableApplication


def new_ui(name):
    def get_gm():
        from bgv.questionaire.theme import GLOBAL_MACROS
        return GLOBAL_MACROS
    return type(name, (UIRegistry,), {'macros': get_gm})()


@dataclass
class Reiter(WrappableApplication):
    ui: UIRegistry = None
    routes: NamedRoutes = field(
        default_factory=partial(NamedRoutes, extractor=routables))

    def get_actions(self, request, classifiers=None):
        return []


app = Reiter(ui=new_ui('BrowserUI'))
backend = Reiter(ui=new_ui('AdminUI'))
