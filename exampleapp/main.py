import time
import threading

import flask

import exampleapp.routes as routes
from exampleapp import tasks

def create_app():

    app = flask.Flask(__name__)

    def stop():
        tasks.running = False
        tasks.thr.join()
    app.stop = stop

    tasks.thr = threading.Thread(target=tasks.thr_fun)
    tasks.thr.start()

    app.register_blueprint(routes.routes)

    return app
