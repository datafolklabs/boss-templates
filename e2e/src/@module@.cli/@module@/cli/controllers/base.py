
import drest
from cement2.core.controller import CementBaseController, expose

class @class_prefix@AbstractBaseController(CementBaseController):
    def _setup(self, app):
        super(@class_prefix@AbstractBaseController, self)._setup(app)
    
class @class_prefix@BaseController(@class_prefix@AbstractBaseController):
    class Meta:
        label = 'base'
        description = '@project@ Base Controller'
        arguments = [
            (['--foo'], dict(help="the notorious foo option."))
            ]
        
    @expose(hide=True)
    def default(self):
        pass