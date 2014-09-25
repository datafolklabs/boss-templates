#!/usr/bin/env python
#
# @description@
#
# Created by: @creator@ <@email@>
# License: @license@
# Url: @url@
#

from cement.core import foundation
from cement.utils.misc import init_defaults
from cement.core.controller import CementBaseController, expose
from cement.core.exc import FrameworkError, CaughtSignal

defaults = init_defaults('@module@')
defaults['@module@'] = dict(
    debug=False,
    foo='bar',
    )

class @class_prefix@BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = '@module@ base controller'.capitalize()
        arguments = [
            ( ['-f', '--foo'], dict(help='the notorious foo option')),
            ]

    @expose(hide=True)
    def default(self):
        print "Inside @class_prefix@BaseController.default()"

class @class_prefix@App(foundation.CementApp):
    class Meta:
        label = '@module@'
        base_controller = @class_prefix@BaseController
        config_defaults = defaults


app = @class_prefix@App()

def main():
    try:
        # Default our exit status to 0 (non-error)
        code = 0

        # Setup the application
        app.setup()

        # Run the application
        app.run()
    except FrameworkError as e:
        # Catch framework errors and exit 1 (error)
        code = 1
        print(e)
    except CaughtSignal as e:
        # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
        code = 0
        print(e)
    finally:
        # Print an exception (if it occurred) and --debug was passed
        if app.debug:
            import sys
            import traceback

            exc_type, exc_value, exc_traceback = sys.exc_info()
            if exc_traceback is not None:
                traceback.print_exc()

        # Close the application
        app.close(code)

if __name__ == '__main__':
    main()
