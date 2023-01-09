import requests, vt, os
from virusapi import test
from flask import Flask, render_template
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
    @app.route('/', methods=('GET','POST'))
    def Startup():
        exec(open("../app/virusapi/test.py").read())
        return render_template('base.html')

    @app.route('/threatanalysis/<status>')
    def APICall(status):
        exec(open("../app/virusapi/test.py").read())
        return render_template('base.html',test=test)
    @app.route('/test')
    def test():
        return render_template('test.html')
    


    return app