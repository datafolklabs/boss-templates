"""Testing utilities for @project@."""

from @module@.cli.main import @class_prefix@TestApp
from cement.utils.test import *

class @class_prefix@TestCase(CementTestCase):
    app_class = @class_prefix@TestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(@class_prefix@TestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(@class_prefix@TestCase, self).tearDown()

