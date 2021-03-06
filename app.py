import os
from flask_route import *

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 33507))

    METEOCONCEPT_TOKEN = None if app.config['ENV'] == 'development' else None
    WEATHERSTACK_TOKEN = None if app.config['ENV'] == 'development' else None

    # On Linux or MAC 'export METEOCONCEPT_TOKEN=...' (check shell echo $METEOCONCEPT_TOKEN)
    # On Windows 'set METEOCONCEPT_TOKEN=...' (check on Powershell echo $Env:METEOCONCEPT_TOKEN)
    app.config['METEOCONCEPT_TOKEN'] = os.environ.get('METEOCONCEPT_TOKEN', METEOCONCEPT_TOKEN)
    app.config['WEATHERSTACK_TOKEN'] = os.environ.get('WEATHERSTACK_TOKEN', WEATHERSTACK_TOKEN)
    app.config['SECRET_KEY'] = 'secret_key'
    app.run(host='0.0.0.0', port=PORT, debug=False)
