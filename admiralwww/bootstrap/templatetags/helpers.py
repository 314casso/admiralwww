# -*- coding: utf-8 -*-
from django import template
from django.utils.safestring import mark_safe
import random
from bootstrap.models import Params
from admiralwww.local_settings import SERVICES
from rdoc.models import DocCategory
register = template.Library()

EMAIL = 'email'

@register.filter()
def hide_email(email):    
    name = email
    mailto_link = u'<a href="mai\'+\'lto:%s">%s</a>' % (encode_string(email), encode_string(name))

    value = '<script type="text/javascript">// <![CDATA['+"\n \
           \tdocument.write('%s')\n \
           \t// ]]></script>\n" % (mailto_link)
    return mark_safe(value.strip())

def encode_string(value):
    """
    Encode a string into it's equivalent html entity.
    
    The tag will randomly choose to represent the character as a hex digit or
    decimal digit.
    """    
    e_string = "" 
    for a in value:
        t = random.randint(0,1)
        if t:
            en = "&#x%x;" % ord(a)
        else:
            en = "&#%d;" % ord(a)
        e_string += en 
    return e_string


@register.simple_tag
def get_param(key, param_type=None):    
    try:    
        p = Params.objects.get(key=key)
        if param_type == EMAIL:
            return hide_email(p.value)
        return p.value    
    except Params.DoesNotExist:
        return ""
    
    
@register.assignment_tag
def get_services():    
    return SERVICES    


@register.assignment_tag
def get_category(slug):
    try:
        return DocCategory.objects.get(slug=slug)    
    except:
        pass