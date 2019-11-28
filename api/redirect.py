import flask

app = flask.Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return flask.redirect("www.google.com")
