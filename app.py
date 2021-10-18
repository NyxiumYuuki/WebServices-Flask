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


app = Flask(__name__)


@app.route('/config')
def config():  # put application's code here
    return str(INDENT) + str(WEATHER) + str(WINDDIRS)


@app.route('/')
def index():
    return render_template('index.html')


# Recherche d'une ville
@app.route('/searchCity', methods=['POST', 'GET'])
def searchCity():  # put application's code here
    if request.method == 'POST':
        search = request.form['search']
    else:
        search = request.args.get('search')

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
        return json.dumps(cities, indent=INDENT, sort_keys=True)


# Informations sur la Ville
@app.route('/city', methods=['POST', 'GET'])
def getCity():  # put application's code here
    if request.method == 'POST':
        insee = request.form['insee']
    else:
        insee = request.args.get('insee')

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
        return json.dumps(city, indent=INDENT, sort_keys=True)


# Information sur la ville et Ephéméride
@app.route('/ephemeride', methods=['POST', 'GET'])
def ephemeride():  # put application's code here
    if request.method == 'POST':
        insee = request.form['insee']
    else:
        insee = request.args.get('insee')

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
        return json.dumps(cityEph, indent=INDENT, sort_keys=True)


# Information sur les alentours d'une ville
@app.route('/around', methods=['POST', 'GET'])
def around():  # put application's code here
    if request.method == 'POST':
        insee = request.form['insee']
        radius = request.form['radius']
    else:
        insee = request.args.get('insee')
        radius = request.args.get('radius')

    if METEOCONCEPT_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN not passed'
    elif insee is None or radius is None:
        log('GET/POST insee or radius variable not passed')
        return 'GET/POST insee or radiu variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN passed')
        with closing(urlopen(API_OBSERVATIONS_AROUND + API_TOKEN + METEOCONCEPT_TOKEN + API_INSEE + insee + API_RADIUS + radius)) as f:
            around = json.loads(f.read())
        return json.dumps(around, indent=INDENT, sort_keys=True)


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 33507))
    # On Linux or MAC 'export METEOCONCEPT_TOKEN=...' (check shell echo $METEOCONCEPT_TOKEN)
    # On Windows 'set METEOCONCEPT_TOKEN=...' (check on Powershell echo $Env:METEOCONCEPT_TOKEN)
    METEOCONCEPT_TOKEN = os.environ.get('METEOCONCEPT_TOKEN', None)
    app.run(host='0.0.0.0', port=PORT, debug=True)