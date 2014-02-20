"""@project.title@ main application entry point."""

from cement.core import foundation
from cement.utils.misc import init_defaults
from cement.core.exc import FrameworkError, CaughtSignal
from @module@.core import exc

# application default.  Should update config/@module@.conf to reflect any
# changes, or additions here.
defaults = init_defaults('@module@')

# all internal/external plugin configurations are loaded from here
defaults['@module@']['plugin_config_dir'] = '/etc/@module@/plugins.d'

# external plugins (generally, do not ship with application code)
defaults['@module@']['plugin_dir'] = '/var/lib/@module@/plugins'

# external templates (generally, do not ship with application code)
defaults['@module@']['template_dir'] = '/var/lib/@module@/templates'


class @class_prefix@App(foundation.CementApp):
    class Meta:
        label = '@module@'
        config_defaults = defaults

        # all built-in application bootstrapping (always run)
        bootstrap = '@module@.cli.bootstrap'

        # optional plugin bootstrapping (only run if plugin is enabled)
        plugin_bootstrap = '@module@.cli.plugins'

        # internal templates (ship with application code)
        template_module = '@module@.cli.templates'

        # internal plugins (ship with application code)
        plugin_bootstrap = '@module@.cli.plugins'


class @class_prefix@TestApp(@class_prefix@App):
    """A test app that is better suited for testing."""
    class Meta:
        argv = []
        config_files = []


# define the applicaiton object outside of main, as some libraries might wish
# to import it as a global (rather than passing it into another class/func)
app = @class_prefix@App()

def main():
    try:
        app.setup()
        app.run()
    except exc.@class_prefix@Error as e:
        print(e)
    except FrameworkError as e:
        print(e)
    except CaughtSignal as e:
        print(e)
    finally:
        app.close()

if __name__ == '__main__':
    main()
