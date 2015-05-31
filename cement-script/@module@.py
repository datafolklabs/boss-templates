#!/usr/bin/env python
#
# @description@
#
# Created by: @creator@ <@email@>
# License: @license@
# Url: @url@
#

from cement.core.foundation import CementApp
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
        description = '@description@'
        arguments = [
            ( ['-f', '--foo'], dict(help='the notorious foo option')),
            ]

    @expose(hide=True)
    def default(self):
        print "Inside @class_prefix@BaseController.default()"

class @class_prefix@App(CementApp):
    class Meta:
        label = '@module@'
        base_controller = @class_prefix@BaseController
        config_defaults = defaults

def main():
    with @class_prefix@App() as app:
        try:
            app.run()
        
        except FrameworkError as e:
            # Catch framework errors and exit 1 (error)
            print('FrameworkError > %s' % e)
            app.exit_code = 1
            
        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('CaughtSignal > %s' % e)
            app.exit_code = 0

if __name__ == '__main__':
    main()
