
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization

class @class_prefix@Authentication(ApiKeyAuthentication):
    """
    TastyPie ApiAuthentication plus web based authentication (allowing
    javascript access from the browser to use the cookie auth).
    """
    def __init__(self):
        super(@class_prefix@Authentication, self).__init__()

    def is_authenticated(self, request, **kwargs):
        if request.user.is_authenticated():
            return True

        return super(@class_prefix@Authentication, self).is_authenticated(request, **kwargs)

class @class_prefix@Authorization(DjangoAuthorization):
    def __init__(self, *args, **kw):
        super(@class_prefix@Authorization, self).__init__(*args, **kw)