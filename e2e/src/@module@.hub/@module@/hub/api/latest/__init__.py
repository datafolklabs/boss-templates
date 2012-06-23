
from tastypie.api import Api

# @boss.mark:hub_import_resources@
from . import accounts
from . import examples

api = Api(api_name='v0')

# @boss.mark:hub_register_resources@
api.register(accounts.UserResource())
api.register(accounts.ProfileResource())
api.register(examples.ExampleResource())

