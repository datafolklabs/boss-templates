
from cement2.core.controller import expose
from @module@.cli.controllers.base import @class_prefix@AbstractBaseController

class @class_prefix@ExampleController(@class_prefix@AbstractBaseController):
    class Meta:
        label = 'example'
        description = '@project@ Example Controller'
        stacked_on = 'base'
        arguments = [
            ( ['-E'], dict(help='the big E option', action='store_true') ),
            ]
        
    def __init__(self, *args, **kw):
        super(@class_prefix@AbstractBaseController, self).__init__(*args, **kw)

    @expose()
    def example_cmd(self):
        pass