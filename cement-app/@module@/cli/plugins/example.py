"""Example Plugin for @project.title@."""

from cement.core.controller import CementBaseController, expose
from cement.core import handler, hook

def example_plugin_hook(app):
    # do something with the ``app`` object here.
    pass

class ExamplePluginController(CementBaseController):
    class Meta:
        # name that the controller is displayed at command line
        label = 'example'

        # text displayed next to the label in ``--help`` output
        description = 'this is an example plugin controller'

        # stack this controller on-top of ``base`` (or any other controller)
        stacked_on = 'base'

        # determines whether the controller is nested, or embedded
        stacked_type = 'nested'

        # these arguments are only going to display under
        # ``$ @module@ example --help``
        arguments = [
            (
                ['-f', '--foo'],
                dict(
                    help='Notorious foo option',
                    action='store',
                    )
            )
        ]

    @expose(help="this is an example sub-command.")
    def example_plugin_command(self):
        print("Inside ExamplePluginController.example_plugin_command().")


def load():
    # register the plugin class.. this only happens if the plugin is enabled
    handler.register(ExamplePluginController)

    # register a hook (function) to run after arguments are parsed.
    hook.register('post_argument_parsing', example_plugin_hook)
