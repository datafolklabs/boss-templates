
import drest
from cement2.core.controller import CementBaseController, expose
from @module@.core import exc

class @class_prefix@AbstractBaseController(CementBaseController):
    def _setup(self, app):
        super(@class_prefix@AbstractBaseController, self)._setup(app)

    def _dispatch(self, *args, **kw):
        # shortcut to the hub for just this resource controller
        if not hasattr(self.app, 'hub'):
            raise exc.@class_prefix@RuntimeError("@project@ hub is inaccessible.")

        self.resource = getattr(self.app.hub, self._meta.label)
        super(@class_prefix@AbstractBaseController, self)._dispatch(*args, **kw)
        
    @expose(hide=True)
    def default(self):
        raise exc.@class_prefix@ArgumentError("A sub-command is required.")
        
    @expose(help="list all available resources")
    def list(self):
        raise NotImplementedError
        
    @expose(help="display details of a resources", aliases=['show'])
    def details(self):
        raise NotImplementedError
    
    @expose(help="create a new resources")
    def create(self):
        raise NotImplementedError
        
    @expose(help="update an existing resources")
    def update(self):
        raise NotImplementedError
        
    @expose(help="delete an existing resources")
    def delete(self):
        raise NotImplementedError    
    
class @class_prefix@BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = '@project@ Base Controller'
        arguments = [
            (['--foo'], dict(help="the notorious foo option."))
            ]
        
    @expose(hide=True)
    def default(self):
        raise exc.@class_prefix@ArgumentError("A sub-command is required.")