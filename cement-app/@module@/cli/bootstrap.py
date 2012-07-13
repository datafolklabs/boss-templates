
from cement.core import handler
from @module@.cli.controllers.base import @class_prefix@BaseController
from @module@.cli.controllers.example import @class_prefix@ExampleController

def load():
    handler.register(@class_prefix@BaseController)
    handler.register(@class_prefix@ExampleController)