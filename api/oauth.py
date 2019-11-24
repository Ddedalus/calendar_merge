from os import environ

import flask
from google_auth_oauthlib.flow import Flow

# scopes requested by the app
scopes = ["https://www.googleapis.com/auth/calendar.events"]


app = flask.Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def oauth(path):
    """ Perform the OAuth2.0 authentication request"""
    return ("Redirected to:", path)
    flow = Flow.from_client_config(client_config(), scopes)
    flow.redirect_uri = "https://calendarmerge.now.sh/oauth_landing"

    authorization_url, state = flow.authorization_url(access_type="offline")
    print("state:", state)

    return flask.Response(authorization_url, mimetype='plain/text')


def client_config():
    return {
        "web": {
            "client_id": environ["CLIENT_ID"],
            "project_id": "h-calendar-merge",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": environ["CLIENT_SECRET"],
            "redirect_uris": [
                "http://localhost:8080/",
                "https://calendarmerge.now.sh/oauth_landing",
            ],
            "javascript_origins": [
                "http://localhost:8080/",
                "https://calendarmerge.now.sh",
            ],
        }
    }
