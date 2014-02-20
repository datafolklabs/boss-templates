"""
@plugin.capitalize@ plugin for @project.title@.

Created by: @creator@ <@email@>
License: @license@
URL: @url@

"""

from cement.core import handler
from cement.core.controller import CementBaseController, expose

class @class_prefix@PluginController(CementBaseController):
    class Meta:
        label = "@plugin@"
        description = "@plugin.capitalize@ Plugin for @project.title@."

def load():
    handler.register(@class_prefix@PluginController)

