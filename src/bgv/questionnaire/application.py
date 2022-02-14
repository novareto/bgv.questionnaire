from functools import partial
from dataclasses import dataclass, field
from reiter.ui.registry import UIRegistry
from reiter.view.utils import routables
from roughrider.routing.components import NamedRoutes
from roughrider.application import WrappableApplication


@dataclass
class Reiter(WrappableApplication):
    ui: UIRegistry = field(default_factory=UIRegistry)
    routes: NamedRoutes = field(
        default_factory=partial(NamedRoutes, extractor=routables))

    def get_actions(self, request, classifiers=None):
        return []


app = Reiter()
