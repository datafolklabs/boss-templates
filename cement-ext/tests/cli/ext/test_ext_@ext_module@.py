"""@ext_module.capitalize@ Framework Extension Tests."""

from cement.utils import test

class @class_prefix@ExtTestCase(test.CementTestCase):
    def setUp(self):
        super(@class_prefix@ExtTestCase, self).setUp()
        self.app = self.make_app('tests',
            extensions=['@package@.cli.ext.@ext_module@'],
            )

    def test_@ext_module@(self):
        self.app.setup()
        self.app.run()

        ### DO SOMETHING TO TEST @ext_module@

        self.app.close()
