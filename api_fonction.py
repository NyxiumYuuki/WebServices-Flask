from config import *
from contextlib import closing
from urllib.request import urlopen
import json


def getSearch(query):
    if METEOCONCEPT_TOKEN is None and WEATHERSTACK_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed'
    elif query is None:
        log('GET/POST search variable not passed')
        return 'GET/POST search variable not passed'
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


def getCurrent(query):
    if METEOCONCEPT_TOKEN is None and WEATHERSTACK_TOKEN is None:
        log('Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed')
        return 'Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed'
    elif query is None:
        log('GET/POST query variable not passed')
        return 'GET/POST query variable not passed'
    else:
        log('Env variable METEOCONCEPT_TOKEN or/and WEATHERSTACK_TOKEN passed')
        try:
            query = int(query)
            with closing(urlopen(
                    API_OBSERVATIONS_AROUND_METEOCONCEPT +
                    API_TOKEN_METEOCONCEPT +
                    METEOCONCEPT_TOKEN +
                    API_INSEE_METEOCONCEPT +
                    str(query) +
                    API_RADIUS_METEOCONCEPT +
                    '0')) as f:
                around_METEOCONCEPT = json.loads(f.read())
            return {"query": query, "around": {
                "METEOCONCEPT": around_METEOCONCEPT,
                "WEATHERSTACK": None
                }
            }
        except:
            with closing(urlopen(
                    API_OBSERVATIONS_AROUND_WEATHERSTACK +
                    API_TOKEN_WEATHERSTACK +
                    WEATHERSTACK_TOKEN +
                    API_SEARCH_WEATHERSTACK +
                    query + ",France")) as f:
                around_WEATHERSTACK = json.loads(f.read())
            return {"query": query, "around": {
                "METEOCONCEPT": None,
                "WEATHERSTACK": around_WEATHERSTACK
                }
            }



# def getEphemeride(insee):
#     if METEOCONCEPT_TOKEN is None:
#         log('Env variable METEOCONCEPT_TOKEN not passed')
#         return 'Env variable METEOCONCEPT_TOKEN not passed'
#     elif insee is None:
#         log('GET/POST insee variable not passed')
#         return 'GET/POST insee variable not passed'
#     else:
#         log('Env variable METEOCONCEPT_TOKEN passed')
#         with closing(urlopen(API_EPHEMERIDE + API_TOKEN + METEOCONCEPT_TOKEN + API_INSEE + insee)) as f:
#             cityEph = json.loads(f.read())
#         return [insee, cityEph]
#
#
# def getCity(insee):
#     if METEOCONCEPT_TOKEN is None and WEATHERSTACK_TOKEN is None:
#         log('Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed')
#         return 'Env variable METEOCONCEPT_TOKEN and WEATHERSTACK_TOKEN not passed'
#     elif search is None:
#         log('GET/POST search variable not passed')
#         return 'GET/POST search variable not passed'
#     else:
#         log('Env variable METEOCONCEPT_TOKEN or/and WEATHERSTACK_TOKEN passed')
#
#         with closing(urlopen(API_LOCATION_CITY + API_TOKEN + METEOCONCEPT_TOKEN + API_INSEE + insee)) as f:
#             city = json.loads(f.read())['city']
#         return [insee, city]
