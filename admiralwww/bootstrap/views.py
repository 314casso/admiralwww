# Create your views here.
from django.shortcuts import render
from bootstrap.models import PortRate

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
    
#     cell_rates = []    
    for rate in port_rates:        
        rates = [rate.not_dangerous_20, rate.not_dangerous_40, rate.dangerous_20, rate.dangerous_40, rate.ref_40]
        colspan_rates = []
        for prev, item, next in neighborhood(rates):
            if item != prev:
                colspan_rates.append({'rate': item, 'colspan':1})
            else:
                colspan_rates[-1]['colspan'] += 1            
                             
        rate.colspan_rates = colspan_rates
                
#         cell_rates.append({'rate': rate.not_dangerous_20, 'colspan':0})
#         if rate.not_dangerous_20 == rate.not_dangerous_40:            
#             cell_rates[-1].colspan += 1
#         else:
#             cell_rates.append({'rate': rate.not_dangerous_40, 'colspan':0})            
#         
#         if rate.not_dangerous_40 == rate.dangerous_20:
#             cell_rates[-1].colspan += 1
#         else:
#             cell_rates.append({'rate': rate.dangerous_20, 'colspan':0})
#             
#         if rate.dangerous_20 == rate.dangerous_40:
#             cell_rates[-1].colspan += 1
#         else:
#             cell_rates.append({'rate': rate.dangerous_40, 'colspan':0})
#             
#         if rate.dangerous_20 == rate.dangerous_40:
#             cell_rates[-1].colspan += 1
#         else:
#             cell_rates.append({'rate': rate.dangerous_40, 'colspan':0})    
        
        
             
        
    return render(request, 'nmcc/port_services.html', {'services': port_rates})
      
    