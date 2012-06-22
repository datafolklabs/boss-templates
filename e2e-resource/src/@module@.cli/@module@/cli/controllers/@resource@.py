
from cement2.core.controller import expose
from @module@.cli.controllers.base import @class_prefix@AbstractBaseController

class @resource.capitalize@Controller(@class_prefix@AbstractBaseController):
    class Meta:
        label = @resource@

    @expose()
    def list(self):
        pass
    
    @expose()
    def details(self):
        pass
        
    @expose()
    def create(self):
        pass
    
    @expose()
    def update(self):
        pass
    
    @expose()
    def delete(self):
        pass