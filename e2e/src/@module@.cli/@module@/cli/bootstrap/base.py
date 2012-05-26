"""@project@ base controller."""

import drest
from cement2.core import hook, handler

@hook.register(name='cement_post_setup_hook')
def attach_hub_object(app):
    try:
        hub = drest.api.TastyPieAPI(app.config.get('@module@', 'hub_api_url'))
        hub.auth(app.config.get('@module@', 'hub_api_user'),
                 app.config.get('@module@', 'hub_api_key'))
        app.extend('hub', hub)
    except drest.exc.dRestAPIError as e:
        app.log.fatal(e.msg)
        
# Import any additional bootstrap files here
#
#   from @module@.cli.bootstrap import example
#