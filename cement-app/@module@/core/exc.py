"""@project@ exception classes."""

class @class_prefix@Error(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class @class_prefix@ConfigError(@class_prefix@Error):
    """Config related errors."""
    pass

class @class_prefix@RuntimeError(@class_prefix@Error):
    """Generic runtime errors."""
    pass

class @class_prefix@ArgumentError(@class_prefix@Error):
    """Argument related errors."""
    pass
