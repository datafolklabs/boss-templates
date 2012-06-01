
from tastypie.api import Api
from @module@.hub.api.version0 import auth, resources

v0_api = Api(api_name='v0')
v0_api.register(resources.UserResource())
v0_api.register(resources.ProfileResource())
v0_api.register(resources.ExampleResource())