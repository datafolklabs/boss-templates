"""@project@ bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as @class_prefix@BaseController.

from @module@.cli.controllers.base import @class_prefix@BaseController

def load(app):
    app.handler.register(@class_prefix@BaseController)
