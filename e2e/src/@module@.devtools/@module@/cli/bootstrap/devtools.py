"""@project@ devtools plugin bootstrap entry point."""

from cement2.core import handler
from @module@.cli.controllers.devtools import @class_prefix@DevtoolsController

handler.register(@class_prefix@DevtoolsController)