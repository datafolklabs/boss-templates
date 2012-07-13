
from cement.core import foundation, backend
from cement.core import exc as cement_exc
from @module@.core import exc

class @class_prefix@App(foundation.CementApp):
    class Meta:
        label = '@module@'

app = @class_prefix@App()

def main():
    try:
        from @module@.cli.bootstrap import base
        app.setup()
        app.run()
    except cement_exc.CementRuntimeError as e:
        raise exc.@class_prefix@RuntimeError(e.msg)
    except cement_exc.CementConfigError as e:
        raise exc.@class_prefix@ConfigError(e.msg)
    except cement_exc.CementArgumentError as e:
        raise exc.@class_prefix@ArgumentError(e.msg)
    except cement_exc.CementInterfaceError as e:
        raise exc.@class_prefix@InterfaceError(e.msg)
    finally:
        app.close()
    
if __name__ == '__main__':
    main()