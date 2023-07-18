import requests, os, werkzeug, json
from flask import Flask, render_template, redirect, request, url_for





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
    @app.route('/', methods=['GET','POST'])
    def Startup():
        return render_template('index.html')
    @app.route('/generator', methods=['GET','POST'])
    def gen():
        return render_template('base.html')
    @app.route('/404')
    def errorpage():
        return render_template('404.html')
    @app.route('/UserPayload', methods=['GET','POST'])
    def APICall():
            API_TOKEN = ("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")
            global payload
            payload = request.form.get('UserPayload')
            print(payload)
            headers = {"Authorization": f"Bearer {API_TOKEN}"}
            API_URL = "https://api-inference.huggingface.co/models/1ostic/gpt2-DrSuess-generators"
            def query(payload):
                data = json.dumps(payload)
                global response
                response = requests.request("POST", API_URL, headers=headers, data=data)
                return json.loads(response.content.decode("utf-8"))
            data = query(payload)
            for x in data:
                modelresponse = x["generated_text"]
                generatedtext = []
                generatedtext.append(modelresponse)

                
                return redirect(url_for('results',generatedtext=generatedtext))
    @app.route('/results/<generatedtext>')
    def results(generatedtext):
        return render_template('results.html',  generatedtext=generatedtext)


    return app