"""Tests for Example Plugin."""

from @module@.utils import test

class ExamplePluginTestCase(test.@class_prefix@TestCase):
    def test_load_example_plugin(self):
        self.app.setup()
        self.app.plugin.load_plugin('example')
