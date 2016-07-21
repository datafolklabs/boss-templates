"""@project@ main application entry point."""

from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults
from cement.core.exc import FrameworkError, CaughtSignal
from @module@.core import exc

# Application default.  Should update config/@module@.conf to reflect any
# changes, or additions here.
defaults = init_defaults('@module@')

# All internal/external plugin configurations are loaded from here
defaults['@module@']['plugin_config_dir'] = '/etc/@module@/plugins.d'

# External plugins (generally, do not ship with application code)
defaults['@module@']['plugin_dir'] = '/var/lib/@module@/plugins'

# External templates (generally, do not ship with application code)
defaults['@module@']['template_dir'] = '/var/lib/@module@/templates'


class @class_prefix@App(CementApp):
    class Meta:
        label = '@module@'
        config_defaults = defaults

        # All built-in application bootstrapping (always run)
        bootstrap = '@module@.cli.bootstrap'

        # Internal plugins (ship with application code)
        plugin_bootstrap = '@module@.cli.plugins'

        # Internal templates (ship with application code)
        template_module = '@module@.cli.templates'

        # call sys.exit() when app.close() is called
        exit_on_close = True


class @class_prefix@TestApp(@class_prefix@App):
    """A test app that is better suited for testing."""
    class Meta:
        # default argv to empty (don't use sys.argv)
        argv = []

        # don't look for config files (could break tests)
        config_files = []

        # don't call sys.exit() when app.close() is called in tests
        exit_on_close = False


# Define the applicaiton object outside of main, as some libraries might wish
# to import it as a global (rather than passing it into another class/func)
app = @class_prefix@App()

def main():
    with app:
        try:
            app.run()
        
        except exc.@class_prefix@Error as e:
            # Catch our application errors and exit 1 (error)
            print('@class_prefix@Error > %s' % e)
            app.exit_code = 1
            
        except FrameworkError as e:
            # Catch framework errors and exit 1 (error)
            print('FrameworkError > %s' % e)
            app.exit_code = 1
            
        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('CaughtSignal > %s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
