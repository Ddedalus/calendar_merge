import logging

import flask

app = flask.Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    # landing page after user completes the OAuth flow with Google

    logging.warning(f"request meat: \n\n {flask.request.values} \n\n")
    return flask.Response(str(flask.request), type="text/plain")
