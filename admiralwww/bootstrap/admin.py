from django.contrib import admin
from bootstrap.models import Params, PortServicie, Nds, Measure, PortRate


class ParamsAdmin(admin.ModelAdmin):
    list_display = ('key', 'hint')


class PortServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'measure', 'nds')


class PortRateAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'not_dangerous_20', 'not_dangerous_40', 'dangerous_20', 'dangerous_40', 'ref_40', 'sort_order')
         

#admin.site.register(Nds)
#admin.site.register(Measure)

admin.site.register(Params, ParamsAdmin)
#admin.site.register(PortServicie, PortServiceAdmin)
#admin.site.register(PortRate, PortRateAdmin)