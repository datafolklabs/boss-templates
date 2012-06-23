
from cement2.core.controller import expose
from @module@.cli.controllers.base import @class_prefix@AbstractBaseController

class @resource.capitalize@Controller(@class_prefix@AbstractBaseController):
    class Meta:
        label = '@plural_resource@'
        description = "@plural_resource.capitalize@ Controller"
