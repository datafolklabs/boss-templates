
from cement.core import handler
from @module@.cli.controllers.base import @class_prefix@BaseController

handler.register(@class_prefix@BaseController)

# Import all permanent plugins here
from @module@.cli.bootstrap import example
