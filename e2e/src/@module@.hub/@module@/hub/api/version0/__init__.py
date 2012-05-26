
from tastypie.api import Api
from @module@.hub.api.version0 import resources

api = Api(api_name='v0')
api.register(resources.UserResource())
api.register(resources.ExampleResource())