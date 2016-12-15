# -*- coding: utf-8 -*-
from django.shortcuts import render
from bootstrap.models import PortRate, Params
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.template import loader, Context
from django.core.mail.message import EmailMessage
from django.utils.encoding import force_unicode
from django.contrib.sites.models import get_current_site
from django.http import HttpResponse
from admiralwww.local_settings import DEFAULT_FROM_EMAIL, SERVICES
from admiralwww.settings import DEBUG
from django.views.generic.base import TemplateView

def neighborhood(iterable):
    iterator = iter(iterable)
    prev = None
    item = iterator.next()  # throws StopIteration if empty.
    for next in iterator:
        yield (prev,item,next)
        prev = item
        item = next
    yield (prev,item,None)

def port_services(request):
    port_rates = list(PortRate.objects.all())
    
    for rate in port_rates:        
        rates = [rate.not_dangerous_20, rate.not_dangerous_40, rate.dangerous_20, rate.dangerous_40, rate.ref_40]
        colspan_rates = []
        for prev, item, next in neighborhood(rates):
            if item != prev:
                colspan_rates.append({'rate': item, 'colspan':1})
            else:
                colspan_rates[-1]['colspan'] += 1            
                             
        rate.colspan_rates = colspan_rates
        
    return render(request, 'nmcc/port_services.html', {'services': port_rates})
     


@require_http_methods(["POST"])
@csrf_exempt
def send_email(request): 
    service = SERVICES.get(request.POST['service'].replace('-','_'))
    COMMERCE_EMAIL = 'commerce_email'
    p = Params.objects.get(key=COMMERCE_EMAIL)
    if DEBUG:
        mailto = 'it-support2@ruscon.global'    
    else:
        mailto = p.value        
    reply_email = request.POST['email']
    t = loader.get_template(service['template'])
    c = Context(request.POST)
    c.update(
             {
              'site': get_current_site(request),
              'service': service['name'],
             }
             )    
    rendered = t.render(c)
    headers = {'Reply-To': reply_email}
    email = EmailMessage(
        force_unicode(service['name']),
        force_unicode(rendered),
        DEFAULT_FROM_EMAIL,
        [mailto],
        headers=headers        
    )
    email.send(False)
    return HttpResponse('SUCCESS')     