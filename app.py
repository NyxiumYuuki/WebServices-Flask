import os
import sys

from flask import Flask, request
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
def hello_world():  # put application's code here
    return 'Hello World!'


# TODO Recherche d'une ville
@app.route('/searchCity', methods=['POST', 'GET'])
def searchCity():  # put application's code here
    if request.method == 'POST':
        city = request.form['search']
    else:
        city = request.args.get('search')
    with closing(urlopen(API_LOCATION_CITIES + API_TOKEN + METEOCONCEPT_TOKEN + API_SEARCH + city)) as f:
        cities = json.loads(f.read())['cities']
    return json.dumps(cities, indent=INDENT, sort_keys=True)


# TODO Informations sur la Ville

# TODO Information sur la ville et Ephéméride

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 33507))
    # On Linux or MAC 'export METEOCONCEPT_TOKEN=...' (check shell echo $METEOCONCEPT_TOKEN)
    # On Windows 'set METEOCONCEPT_TOKEN=...' (check on Powershell echo $Env:METEOCONCEPT_TOKEN)
    METEOCONCEPT_TOKEN = int(os.environ.get('METEOCONCEPT_TOKEN', -1))
    if METEOCONCEPT_TOKEN == -1:
        log('Env variable METEOCONCEPT_TOKEN not passed')
        sys.exit(0)
    else:
        log('Env variable METEOCONCEPT_TOKEN passed')
        app.run(host='0.0.0.0', port=PORT, debug=True)
