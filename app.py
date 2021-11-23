import os
from config import *
from flask_route import *

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 33507))
    # On Linux or MAC 'export METEOCONCEPT_TOKEN=...' (check shell echo $METEOCONCEPT_TOKEN)
    # On Windows 'set METEOCONCEPT_TOKEN=...' (check on Powershell echo $Env:METEOCONCEPT_TOKEN)
    METEOCONCEPT_TOKEN = os.environ.get('METEOCONCEPT_TOKEN', METEOCONCEPT_TOKEN)
    WEATHERSTACK_TOKEN = os.environ.get('WEATHERSTACK_TOKEN', WEATHERSTACK_TOKEN)
    app.config['SECRET_KEY'] = 'secret_key'
    app.run(host='0.0.0.0', port=PORT, debug=True)