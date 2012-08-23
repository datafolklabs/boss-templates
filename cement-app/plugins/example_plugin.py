"""@project.title@ example plugin."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler

class ExamplePluginController(CementBaseController):
    class Meta:
        label = 'example_plugin'
        description = 'Example Plugin Controller'
        stacked_on = 'base'
    
    @expose(help="This is an example command.")
    def example_plugin_command(self):
        print("Inside ExamplePluginController.example_plugin_command().")
        
def load():
    handler.register(ExamplePluginController)