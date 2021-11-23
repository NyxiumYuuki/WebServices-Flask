from flask import Flask, request, render_template
from config import *
from forms import *
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
    return app_response(getSearch(query))


# Information sur les alentours d'une ville
@app.route('/current', methods=['POST', 'GET'])
def current():  # put application's code here
    if request.method == 'POST':
        query = request.form['query']
    else:
        query = request.args.get('query')
    return app_response(getCurrent(query))

# # Informations sur la Ville
# @app.route('/city', methods=['POST', 'GET'])
# def getCity():  # put application's code here
#     if request.method == 'POST':
#         insee = request.form['insee']
#     else:
#         insee = request.args.get('insee')
#     return app_response(json.dumps(getCity(insee), indent=INDENT, sort_keys=True))
#
#
# # Information sur la ville et Ephéméride
# @app.route('/ephemeride', methods=['POST', 'GET'])
# def ephemeride():  # put application's code here
#     if request.method == 'POST':
#         insee = request.form['insee']
#     else:
#         insee = request.args.get('insee')
#     return app_response(json.dumps(getEphemeride(insee), indent=INDENT, sort_keys=True))


# @app.route('/', methods=['POST', 'GET'])
# def index():
#     response_cities = False
#     response_ephemeride = False
#     response_around = False
#
#     search = Search()
#     city = City()
#     around = Around()
#
#     if search.submit_search.data and search.validate_on_submit():
#         return render_template('index.html', cities=getApiCity(search))
#
#     if city.submit_city.data and city.validate_on_submit():
#         return render_template('index.html', ephemeride=getEphemeride(city))
#
#     if around.submit_around.data and around.validate_on_submit():
#         return render_template('index.html', around=getAround(around, 1))
#
#         # TODO Multiple form for insee ? or ajax ?
#         insee = request.form['insee']
#         response_ephemeride = getEphemeride(insee)
#         response_around = getAround(insee, 1)
#
#     return render_template('index.html', cities=response_cities, ephemeride=response_ephemeride, around=response_around)