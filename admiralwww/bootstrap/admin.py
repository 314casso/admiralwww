from django.contrib import admin
from bootstrap.models import Params

class ParamsAdmin(admin.ModelAdmin):
    list_display = ('key', 'hint')

admin.site.register(Params, ParamsAdmin)