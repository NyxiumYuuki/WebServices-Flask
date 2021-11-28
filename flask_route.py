from flask import Flask, request, render_template
from api_fonction import *

app = Flask(__name__)


def app_response(results):
    if JSON_PRETTYFIER:
        json_results = json.dumps(results, indent=INDENT, sort_keys=True)
    else:
        json_results = json.dumps(results, sort_keys=True)
    response = app.response_class(
        response=json_results,
        status=200,
        mimetype='application/json'
    )
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/config')
def config():  # put application's code here
    return app_response({})


# Recherche d'une ville
@app.route('/search', methods=['POST', 'GET'])
def search():  # put application's code here
    if request.method == 'POST':
        query = request.form['query']
    else:
        query = request.args.get('query')
    return app_response(getSearch(query, app.config['METEOCONCEPT_TOKEN'], app.config['WEATHERSTACK_TOKEN']))


# Information sur les alentours d'une ville
@app.route('/current', methods=['POST', 'GET'])
def current():  # put application's code here
    if request.method == 'POST':
        query = request.form['query']
    else:
        query = request.args.get('query')
    return app_response(getCurrent(query, app.config['METEOCONCEPT_TOKEN'], app.config['WEATHERSTACK_TOKEN']))

# Prévision pour une ville
@app.route('/forecast', methods=['POST', 'GET'])
def forecast():  # put application's code here
    if request.method == 'POST':
        query = request.form['query']
    else:
        query = request.args.get('query')
    return app_response(getForecast(query, app.config['METEOCONCEPT_TOKEN'], app.config['WEATHERSTACK_TOKEN']))


# Informations sur la Ville
@app.route('/city', methods=['POST', 'GET'])
def city():  # put application's code here
    if request.method == 'POST':
        query = request.form['query']
    else:
        query = request.args.get('query')
    return app_response(getCity(query, app.config['METEOCONCEPT_TOKEN'], app.config['WEATHERSTACK_TOKEN']))


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')