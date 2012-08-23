"""@project.title@ main application entry point."""

from cement.core import foundation, backend
from cement.core.exc import FrameworkError, CaughtSignal
from @module@.core import exc

class @class_prefix@App(foundation.CementApp):
    class Meta:
        bootstrap = '@module@.cli.bootstrap'
        label = '@module@'

class @class_prefix@TestApp(@class_prefix@App):
    """A test app that is better suited for testing."""
    class Meta:
        argv = []
        config_files = []
        
def main():
    app = @class_prefix@App()
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