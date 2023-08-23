from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import requests

def create_app():


    app = Flask(__name__)


    @app.route('/')
    def hello_world():
        return render_template('index.html')
        

    @app.route('/estimerpointure/', methods=["POST"])
    def estimer_pointure():
        taille = request.form['taille']
        URL_API = 'http://127.0.0.1:8000/estimation_pointure/'+str(taille)
        Api = requests.get(url=URL_API)
        return jsonify(Api.text)

    return app


app = create_app()