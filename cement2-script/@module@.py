#!/usr/bin/env python
#
# @description@
#
# Created by: @creator@ <@email@>
# @url@
#

import sys
from cement2.core import foundation, backend
from cement2.core.controller import CementBaseController, expose
from cement2.core import exc as cement_exc

defaults = backend.defaults('@module@')
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
        pass
    
    @expose()
    def sub_command(self):
        pass
        
class @class_prefix@App(foundation.CementApp):
    class Meta:
        label = '@module@'
        base_controller = @class_prefix@BaseController
        config_defaults = defaults
        
app = @class_prefix@App()

def main():
    try:
        app.setup()
        app.run()
    except cement_exc.CementSignalError as e:
        print e.msg
        sys.exit(1)
    finally:
        app.close()
