import flask

from exampleapp import tasks

routes = flask.Blueprint("root", __name__)

@routes.route("/", methods=["GET"])
def get_counter():
    return f"Counter is at {tasks.counter}\n"
