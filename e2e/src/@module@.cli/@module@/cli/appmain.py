"""@project@ primary cli application entry point."""

import sys
import drest
from cement2.core import foundation, backend
from cement2.core import exc as cement_exc
from @module@.core import exc
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
        
app = @class_prefix@CLIApplication()

def main(*args, **kw):
    try:
        # allow internal bootstrapping to happen
        from @module@.cli.bootstrap import base

        app.setup()
        app.run()
    except exc.@class_prefix@ArgumentError as e:
        print e
        sys.exit(1)
    except exc.@class_prefix@ConfigError as e:
        print e
        sys.exit(1)
    except exc.@class_prefix@RuntimeError as e:
        print e
        sys.exit(1)
    except cement_exc.CementSignalError as e:
        print e
        sys.exit(1)
    except drest.exc.dRestRequestError as e:
        print e
        sys.exit(1)
    finally:
        app.close()
