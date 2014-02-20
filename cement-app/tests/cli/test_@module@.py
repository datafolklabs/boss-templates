"""CLI tests for @module@."""

from @module@.utils import test

class CliTestCase(test.@class_prefix@TestCase):
    def test_@module@_cli(self):
        self.app.setup()
        self.app.run()
        self.app.close()
