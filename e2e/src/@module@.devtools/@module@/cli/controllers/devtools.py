"""@project@ devtools controller."""

import os
from cement2.core.controller import expose
from cement2.tools import exec_cmd2, abspath
from @module@.cli.controllers.base import @class_prefix@AbstractBaseController
    
class @class_prefix@DevtoolsController(@class_prefix@AbstractBaseController):
    class Meta:
        label = 'devtools'
        config_section = 'devtools'
        config_defaults = dict(
            source_dir = '~/devel/@module@'
            )

    def _setup(self, app):
        super(@class_prefix@DevtoolsController, self)._setup(app)
        src = abspath(self.app.config.get('devtools', 'source_dir'))
        self.app.config.set('devtools', 'source_dir', src)
                    
    @expose(help="initialize the @module@.hub database (development)")
    def syncdb(self):
        ret = exec_cmd2(['python', 'src/@module@.hub/manage.py', 'syncdb'])
    
    @expose(help='run the hub interface')
    def starthub(self):
        ret = exec_cmd2([
            'python', 'src/@module@.hub/manage.py', 'runserver', '0.0.0.0:8000'
            ])
            
    @expose(help='run the hub interface')
    def loaddata(self):
        ret = exec_cmd2([
            'python', 'src/@module@.hub/manage.py', 'loaddata', 
            'src/@module@.hub/@module@/hub/fixtures/test_data.json'
            ])