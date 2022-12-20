import os, requests, vt

from flask import Flask, render_template
from templates import base


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def APICall():
        client = vt.Client("<29909ddf2acb1233e0cab2142ec6ea733e786e4d97ea4b631e70860acf0c61c6>")
        file = client.get_object("/files/data")
        if requests.method == "POST":
            userfile = requests.form.get("userfile")
            exec(open("test.py").read())
    

    return app