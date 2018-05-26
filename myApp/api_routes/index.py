
# Imports
##########

from flask import current_app
from . import api_routes
import json

###############################################################################

# Routes
#########

@api_routes.route('/')
def index():
	current_app.logger.info('/api/v1/')
	return "this is /api/v1/"

## Dev testing for Factory
@api_routes.route('/ping')
def dummy_api():
	current_app.logger.info('/api/v1/')
	return 'pong'

###############################################################################
