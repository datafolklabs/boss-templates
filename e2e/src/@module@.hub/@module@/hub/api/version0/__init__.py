
from tastypie.api import Api
from @module@.hub.api.version0.resources import user
from @module@.hub.api.version0.resources import profile
from @module@.hub.api.version0.resources import example

v0_api = Api(api_name='v0')
v0_api.register(user.UserResource())
v0_api.register(profile.ProfileResource())
v0_api.register(example.ExampleResource())
# @boss.mark:api_register_resource@