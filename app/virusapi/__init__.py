import requests, os, werkzeug, json
from flask import Flask, render_template, redirect, request
from APIRequests import URLsender



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
    @app.route('/')
    def Startup():
        return render_template('base.html')
    @app.route('/404')
    def errorpage():
        return render_template('404.html')
    @app.route('/UserURL', methods=['GET','POST'])
    def APICall():
        global URL
        URL = request.form['UserURL']
        #try:
        URLsender(URL)
        return render_template('results.html',  data=data)
        #except:
            #return render_template("404.html")

    #@app.route("/")
    #def home():
    #    return render_template("index.html")

    #@app.route("/api_test")
    #def APICall():
    #    if request.method == "GET":
    #        userfile = request.form.get("userfile")
    #        exec(open("test.py").read())
    
    #@app.route("/test")
    #def testing():
    #    render_template("test.html")
    #    return app
    #    exec(open("../app/virusapi/test.py").read())
    #    return render_template('base.html')
    
    #@app.errorhandler(werkzeug.exceptions.HTTPException)
    #def error():
    #    redirect ("/404")
    
    #return app