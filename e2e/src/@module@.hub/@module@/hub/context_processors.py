
from pkg_resources import get_distribution

def template_shortcuts(request):
    from django.conf import settings
    
    cuts = {
        'base' : settings.BASE_URL,
        'version' : get_distribution('@module@.hub').version,
        'js' : '%sjs/' % settings.STATIC_URL,
        'img' : '%simg/' % settings.STATIC_URL,
        'css' : '%scss/' % settings.STATIC_URL,
        }
    return cuts