import pathlib
import importscan
import fanstatic
import http_session
import http_session_file
import reiter.auth.testing
import reiter.auth.components
import reiter.auth.filters
import bgv.questionnaire.browser
import bgv.questionnaire.theme

from functools import partial
from horseman.mapping import Mapping
from roughrider.sqlalchemy.component import SQLAlchemyEngine
from bgv.questionnaire.application import app, backend
from bgv.questionnaire.models import Base as SQLModels


#### Scanning the browser package
importscan.scan(bgv.questionnaire.browser)
importscan.scan(bgv.questionnaire.theme)


session_environ = "session"

session = http_session.SignedCookieManager(
    http_session_file.FileStore(
        pathlib.Path('./sessions'), 3000
    ),
    'secret', salt='salt', cookie_name='cookie', TTL=3000
)

admin_session = http_session.SignedCookieManager(
    http_session_file.FileStore(
        pathlib.Path('./sessions'), 3000
    ),
    'admin-secret', salt='saltier', cookie_name='admincookie', TTL=3000
)

session_getter = reiter.auth.components.session_from_environ(
    session_environ
)

# Auth
authentication = reiter.auth.components.Auth(
    sources=[],
    user_key="principal",
    session_getter=session_getter,
    filters=(
        reiter.auth.filters.security_bypass([
            "/login"
        ]),
        reiter.auth.filters.secured(path="/login"),
    )
)

admin_authentication = reiter.auth.components.Auth(
    sources=[reiter.auth.testing.DictSource({"admin": "admin"})],
    user_key="admin_principal",
    session_getter=session_getter,
    filters=(
        reiter.auth.filters.security_bypass([
            "/login"
        ]),
        reiter.auth.filters.secured(path="/login"),
    )
)

sqlsession = SQLAlchemyEngine.from_url(
    name='sql', url='sqlite:///example.db'
)


#### Registering middlewares.
# Browser
app.middlewares.add(partial(
    session.middleware,
    environ_key=session_environ,
    secure=False
), 20)

app.middlewares.add(sqlsession('sql'), 30)
app.middlewares.add(authentication, 40)

# Backend
backend.middlewares.add(partial(
    admin_session.middleware,
    environ_key=session_environ,
    secure=False
), 20)

backend.middlewares.add(sqlsession('sql'), 30)
backend.middlewares.add(admin_authentication, 40)

#### Registering utilities
app.utilities['authentication'] = authentication
app.utilities['sql'] = sqlsession

backend.utilities['authentication'] = admin_authentication
backend.utilities['sql'] = sqlsession


#### Create tables
SQLModels.metadata.create_all(sqlsession.engine)


#### Routing
router = fanstatic.Fanstatic(
    Mapping({
        "/": app,
        "/backend": backend,
    }),
    compile=True,
    recompute_hashes=True,
    bottom=True,
    publisher_signature="static"
)
