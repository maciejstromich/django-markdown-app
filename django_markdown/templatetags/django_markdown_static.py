from django.conf import settings
from django.template import Library

register = Library()

from django.templatetags.static import static as _static


@register.simple_tag
def static(path):
    return _static(path)
