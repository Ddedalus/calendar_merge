import logging

import flask
from google_auth_oauthlib.flow import Flow

from api.oauth import client_config

app = flask.Flask(__name__)

scopes = ["https://www.googleapis.com/auth/calendar.events"]


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    # landing page after user completes the OAuth flow with Google
    flow = Flow.from_client_config(client_config(), scopes)
    flow.redirect_uri = "https://calendarmerge.now.sh/oauth_landing"

    authorization_url, state = flow.authorization_url(access_type="offline")
    logging.warning(f"state: {state}")
    logging.warning(f"path: {path}")
    logging.warning(f"request: {flask.request}")
    return flask.response(str(flask.request), type="text/plain")
