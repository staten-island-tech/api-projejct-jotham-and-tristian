import requests, os, werkzeug, json
from flask import Flask, render_template, redirect, request





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
    @app.route(f'/UserURL', methods=['GET','POST'])
    def APICall():
        global URL
        URL = request.form['UserURL']
        #try:
        def URLsender(URL):
            url = "https://www.virustotal.com/api/v3/urls"

            payload = (f"url={URL}")
            headers = {
            "accept": "application/json",
            "x-apikey": "29909ddf2acb1233e0cab2142ec6ea733e786e4d97ea4b631e70860acf0c61c6",
            "content-type": "application/x-www-form-urlencoded"
            }


            response = requests.post(url, data=payload, headers=headers)
            responsedata = json.loads(response.text)
            for data in responsedata:
                URLpadded = responsedata["data"]["id"]
                global URLhash
                URLhash = URLpadded[2:66]
            def AnalysisReport(URLhash):
                url = (f"https://www.virustotal.com/api/v3/urls/{URLhash}")

                headers = {
                "accept": "application/json",
                "x-apikey": "29909ddf2acb1233e0cab2142ec6ea733e786e4d97ea4b631e70860acf0c61c6"
                }
                global data1
                response = requests.get(url, headers=headers)
                data1 = json.loads(response.text)
                for x in data1:
                    global result
                    result = data1["data"]["attributes"]["total_votes"]
                

            AnalysisReport(URLhash)
        URLsender(URL)

        return render_template('results.html',  result=result)
        #except:
            #return render_template("404.html")


    return app