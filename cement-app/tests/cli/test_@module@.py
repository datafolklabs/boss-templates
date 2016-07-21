"""CLI tests for @module@."""

from @module@.utils import test

class CliTestCase(test.@class_prefix@TestCase):
    def test_@module@_cli(self):
        argv = ['--foo=bar']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.foo, 'bar')
