from config import *
from contextlib import closing
from urllib.request import urlopen
import json
import sys


def log(*args):
    print(args[0] % (len(args) > 1 and args[1:] or []))
    sys.stdout.flush()


def getSearch(query, METEOCONCEPT_TOKEN, WEATHERSTACK_TOKEN):
    if METEOCONCEPT_TOKEN is None and WEATHERSTACK_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed'
    elif query is None:
        log('GET/POST query variable not passed')
        return 'GET/POST query variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN or/and WEATHERSTACK_TOKEN passed')
        with closing(urlopen(
                API_LOCATION_CITIES_METEOCONCEPT +
                API_TOKEN_METEOCONCEPT +
                METEOCONCEPT_TOKEN +
                API_SEARCH_METEOCONCEPT + query)) as f:
            cities_METEOCONCEPT = json.loads(f.read())['cities']

        with closing(urlopen(
                API_LOCATION_CITIES_WEATHERSTACK +
                API_TOKEN_WEATHERSTACK +
                WEATHERSTACK_TOKEN +
                API_SEARCH_WEATHERSTACK + query)) as f:
            cities_WEATHERSTACK = json.loads(f.read())
        return {"query": query,
                "cities": {
                    "METEOCONCEPT": cities_METEOCONCEPT,
                    "WEATHERSTACK": cities_WEATHERSTACK
                }
                }


def getCurrent(query, METEOCONCEPT_TOKEN, WEATHERSTACK_TOKEN):
    if METEOCONCEPT_TOKEN is None and WEATHERSTACK_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed'
    elif query is None:
        log('GET/POST query variable not passed')
        return 'GET/POST query variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN or/and WEATHERSTACK_TOKEN passed')
        if query.isnumeric():
            insee = int(query)
            with closing(urlopen(
                    API_OBSERVATIONS_AROUND_METEOCONCEPT +
                    API_TOKEN_METEOCONCEPT +
                    METEOCONCEPT_TOKEN +
                    API_INSEE_METEOCONCEPT +
                    str(insee) +
                    API_RADIUS_METEOCONCEPT +
                    '0')) as f:
                around_METEOCONCEPT = json.loads(f.read())[0]
            return {"query": insee, "current": {
                "METEOCONCEPT": around_METEOCONCEPT,
                "WEATHERSTACK": None
            }
                    }
        else:
            with closing(urlopen(
                    API_OBSERVATIONS_AROUND_WEATHERSTACK +
                    API_TOKEN_WEATHERSTACK +
                    WEATHERSTACK_TOKEN +
                    API_SEARCH_WEATHERSTACK +
                    query + ",France")) as f:
                around_WEATHERSTACK = json.loads(f.read())
            return {"query": query, "current": {
                "METEOCONCEPT": None,
                "WEATHERSTACK": around_WEATHERSTACK
            }
                    }

def getForecast(query, METEOCONCEPT_TOKEN, WEATHERSTACK_TOKEN):
    if METEOCONCEPT_TOKEN is None and WEATHERSTACK_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed'
    elif query is None:
        log('GET/POST query variable not passed')
        return 'GET/POST query variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN or/and WEATHERSTACK_TOKEN passed')
        if query.isnumeric():
            insee = int(query)
            with closing(urlopen(
                    API_FORECAST_CITY_METEOCONCEPT +
                    API_TOKEN_METEOCONCEPT +
                    METEOCONCEPT_TOKEN +
                    API_INSEE_METEOCONCEPT +
                    str(insee))) as f:
                forecast_METEOCONCEPT = json.loads(f.read())
            return {"query": insee, "forecast": {
                "METEOCONCEPT": forecast_METEOCONCEPT,
                "WEATHERSTACK": None
            }
                    }
        else:
            return 'WEATHERSTACK not implemented'

def getCity(query, METEOCONCEPT_TOKEN, WEATHERSTACK_TOKEN):
    if METEOCONCEPT_TOKEN is None and WEATHERSTACK_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed'
    elif query is None:
        log('GET/POST query variable not passed')
        return 'GET/POST query variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN or/and WEATHERSTACK_TOKEN passed')
        if query.isnumeric():
            insee = int(query)
            with closing(urlopen(
                    API_LOCATION_CITY_METEOCONCEPT +
                    API_TOKEN_METEOCONCEPT +
                    METEOCONCEPT_TOKEN +
                    API_INSEE_METEOCONCEPT +
                    str(insee))) as f:
                city_METEOCONCEPT = json.loads(f.read())['city']

            return {"query": insee, "city": {
                "METEOCONCEPT": city_METEOCONCEPT,
                "WEATHERSTACK": None
            }
                    }
        else:
            with closing(urlopen(
                    API_OBSERVATIONS_AROUND_WEATHERSTACK +
                    API_TOKEN_WEATHERSTACK +
                    WEATHERSTACK_TOKEN +
                    API_SEARCH_WEATHERSTACK +
                    query + ",France")) as f:
                city_WEATHERSTACK = json.loads(f.read())['location']
            return {"query": query, "city": {
                "METEOCONCEPT": None,
                "WEATHERSTACK": city_WEATHERSTACK
            }
                    }