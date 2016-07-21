"""
@plugin.capitalize@ plugin for @project@.

Created by: @creator@ <@email@>
License: @license@
URL: @url@

"""

from cement.core.controller import CementBaseController, expose

class @class_prefix@PluginController(CementBaseController):
    class Meta:
        label = "@plugin@"
        description = "@plugin.capitalize@ Plugin for @project@."

def load(app):
    app.handler.register(@class_prefix@PluginController)

