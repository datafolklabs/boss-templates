"""@project@ primary cli application entry point."""

import sys
import drest
from cement2.core import foundation, backend
from cement2.core import exc as cement_exc
from @module@.cli.controllers.base import @class_prefix@BaseController

defaults = backend.defaults('@module@')
defaults['@module@'] = dict(
    hub_api_url='http://localhost:8000/api/v0/',
    hub_api_key='XXXXX',
    hub_api_user='john.doe',
    )
    
class @class_prefix@CLIApplication(foundation.CementApp):
    class Meta:
        label = '@module@'
        base_controller = @class_prefix@BaseController
        plugin_bootstrap = '@module@.cli.bootstrap'
        config_defaults = defaults
        
app = @class_prefix@CLIApplication(*args, **kw)

# allow internal bootstrapping to happen
from @module@.cli.bootstrap import base
        
def main(*args, **kw):
    try:
        app.setup()
        app.run()
    except cement_exc.CementSignalError as e:
        print e.msg
        sys.exit(1)
    except drest.exc.dRestRequestError as e:
        print e.msg
        print e.response.data
        sys.exit(1)
    finally:
        app.close()
