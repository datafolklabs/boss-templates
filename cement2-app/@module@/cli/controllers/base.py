
from cement2.core.controller import CementBaseController, expose

class @class_prefix@AbstractBaseController(CementBaseController):
    """
    This is an abstract base controller that all @project@ controllers 
    should sub-class from.  It should not be used directly.
    
    """
    class Meta:
        label = None
        description = None
        arguments = []
        config_section = None
        config_defaults = {}
        epilog = None
        
    def __init__(self, *args, **kw):
        super(@class_prefix@AbstractBaseController, self).__init__(*args, **kw)

class @class_prefix@BaseController(@class_prefix@AbstractBaseController):
    class Meta:
        label = 'base'
        description = '@description@'
        arguments = [
            (   ['-f', '--foo'], 
                dict(help='the notorious foo option', 
                     dest='foo', 
                     action='store',
                     metavar='TEXT') ),
            ]

    @expose(hide=True)
    def default(self):
        pass
    
    @expose(aliases=['cmd1'], help='this command is useless')
    def command1(self):
        pass