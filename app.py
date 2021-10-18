import os
import sys

from flask import Flask, request, render_template
from contextlib import closing
from urllib.request import urlopen
import json
from config import *


# logging helper
def log(*args):
    print(args[0] % (len(args) > 1 and args[1:] or []))
    sys.stdout.flush()


def getApiCity(search):
    if METEOCONCEPT_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN not passed'
    elif search is None:
        log('GET/POST search variable not passed')
        return 'GET/POST search variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN passed')
        with closing(urlopen(API_LOCATION_CITIES + API_TOKEN + METEOCONCEPT_TOKEN + API_SEARCH + search)) as f:
            cities = json.loads(f.read())['cities']
        return [search, cities]


def getAround(insee, radius):
    if METEOCONCEPT_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN not passed'
    elif insee is None or radius is None:
        log('GET/POST insee or radius variable not passed')
        return 'GET/POST insee or radiu variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN passed')
        with closing(
                urlopen(
                    API_OBSERVATIONS_AROUND + API_TOKEN + METEOCONCEPT_TOKEN + API_INSEE + insee + API_RADIUS + radius)) as f:
            around = json.loads(f.read())
        return [insee, radius, around]


def getEphemeride(insee):
    if METEOCONCEPT_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN not passed'
    elif insee is None:
        log('GET/POST insee variable not passed')
        return 'GET/POST insee variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN passed')
        with closing(urlopen(API_EPHEMERIDE + API_TOKEN + METEOCONCEPT_TOKEN + API_INSEE + insee)) as f:
            cityEph = json.loads(f.read())
        return [insee, cityEph]


def getCity(insee):
    if METEOCONCEPT_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN not passed'
    elif insee is None:
        log('GET/POST insee variable not passed')
        return 'GET/POST insee variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN passed')
        with closing(urlopen(API_LOCATION_CITY + API_TOKEN + METEOCONCEPT_TOKEN + API_INSEE + insee)) as f:
            city = json.loads(f.read())['city']
        return [insee, city]


app = Flask(__name__)


@app.route('/config')
def config():  # put application's code here
    return str(INDENT) + str(WEATHER) + str(WINDDIRS)


@app.route('/', methods=['POST', 'GET'])
def index():
    response_cities = False
    response_ephemeride = False
    response_around = False
    if request.method == 'POST':
        search = request.form['search']
        response_cities = getApiCity(search)

        # TODO Multiple form for insee ? or ajax ?
        # insee = request.form['insee']
        # response_ephemeride = getEphemeride(insee)
        # response_around = getAround(insee, 1)

    return render_template('index.html', cities=response_cities, ephemeride=response_ephemeride, around=response_around)


# Recherche d'une ville
@app.route('/searchCity', methods=['POST', 'GET'])
def searchCity():  # put application's code here
    if request.method == 'POST':
        search = request.form['search']
    else:
        search = request.args.get('search')
    return json.dumps(getApiCity(search), indent=INDENT, sort_keys=True)


# Informations sur la Ville
@app.route('/city', methods=['POST', 'GET'])
def getCity():  # put application's code here
    if request.method == 'POST':
        insee = request.form['insee']
    else:
        insee = request.args.get('insee')
    return json.dumps(getCity(insee), indent=INDENT, sort_keys=True)


# Information sur la ville et Ephéméride
@app.route('/ephemeride', methods=['POST', 'GET'])
def ephemeride():  # put application's code here
    if request.method == 'POST':
        insee = request.form['insee']
    else:
        insee = request.args.get('insee')
    return json.dumps(getEphemeride(insee), indent=INDENT, sort_keys=True)


# Information sur les alentours d'une ville
@app.route('/around', methods=['POST', 'GET'])
def around():  # put application's code here
    if request.method == 'POST':
        insee = request.form['insee']
        radius = request.form['radius']
    else:
        insee = request.args.get('insee')
        radius = request.args.get('radius')
    return json.dumps(getAround(insee, radius), indent=INDENT, sort_keys=True)


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 33507))
    # On Linux or MAC 'export METEOCONCEPT_TOKEN=...' (check shell echo $METEOCONCEPT_TOKEN)
    # On Windows 'set METEOCONCEPT_TOKEN=...' (check on Powershell echo $Env:METEOCONCEPT_TOKEN)
    METEOCONCEPT_TOKEN = os.environ.get('METEOCONCEPT_TOKEN', None)
    app.run(host='0.0.0.0', port=PORT, debug=True)
