
class @class_prefix@Error(Exception):
    """Generic @project.capitalize@ Errors."""
    def __init__(self, msg):
        self.msg = msg
    
    def __repr__(self):
        return "<@class_prefix@Error: %s>" % self.msg
    
    def __str__(self):
        return "<@class_prefix@Error: %s>" % self.msg
    
class @class_prefix@ArgumentError(@class_prefix@Error):
    """@project.capitalize@ Argument Errors."""

    def __repr__(self):
        return "@class_prefix@ArgumentError: %s" % self.msg
        
class @class_prefix@RuntimeError(@class_prefix@Error):
    """@project.capitalize@ Runtime Errors."""

    def __repr__(self):
        return "@class_prefix@RuntimeError: %s" % self.msg

class @class_prefix@ConfigError(@class_prefix@Error):
    """@project.capitalize@ Config Errors."""

    def __repr__(self):
        return "@class_prefix@ConfigError: %s" % self.msg
