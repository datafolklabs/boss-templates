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

def main():
    app = @class_prefix@App()
    try:
        app.setup()
        app.run()
    except FrameworkError as e:
        print(e)
    except CaughtSignal as e:
        print(e)
    finally:
        app.close()

if __name__ == '__main__':
    main()
