
from tastypie.api import Api
from . import *

api = Api(api_name='v0')
api.register(accounts.UserResource())
api.register(accounts.ProfileResource())
api.register(examples.ExampleResource())
# @boss.mark:hub_resources@
