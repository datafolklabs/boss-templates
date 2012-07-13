"""@ext_module.capitalize@ Framework Extension Tests."""

import unittest
from nose.tools import eq_, raises
from cement.utils import test_helper as _t

class @class_prefix@ExtTestCase(unittest.TestCase):
    def setUp(self):
        self.app = _t.prep('tests', extensions=['@ext_module@'])
            
    def test_@ext_module@(self):    
        self.app.setup()
        self.app.run()

        ### DO SOMETHING TO TEST @ext_module@

        self.app.close()