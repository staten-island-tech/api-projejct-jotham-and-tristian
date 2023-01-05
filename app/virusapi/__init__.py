import os, requests, vt
from flask import Flask, render_template, request, redirect

exec(open("../app/virusapi/test.py").read())

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
    @app.route("/api_test")
    def APICall():
        if request.method == "GET":
            userfile = request.form.get("userfile")
            exec(open("test.py").read())
    
    @app.route("/test")
    def testing():
        render_template("test.html")
    return app
    exec(open("../app/virusapi/test.py").read())
    return render_template('base.html')
    
    @app.errorhandler(werkzeug.exceptions.HTTPException)
    def error():
        redirect ("/404")