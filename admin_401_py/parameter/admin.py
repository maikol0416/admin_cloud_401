from django.contrib import admin

from .models import *

class DisplayTypeParameter(admin.ModelAdmin):
	list_display=('code','name_type','pub_date','status')
	search_fields=('code','name_type',)

class DisplayParameter(admin.ModelAdmin):
	list_display=('code','name_parameter','type_parameter_fk','pub_date')
	search_fields=('code','name_parameter',)

class DisplayParameterDetail(admin.ModelAdmin):
	list_display=('code','value_parameter','parameter_fk')
	search_fields=('code','value_parameter',)

admin.site.register(TypeParameter,DisplayTypeParameter)
admin.site.register(Parameter,DisplayParameter)
admin.site.register(ParameterDetail,DisplayParameterDetail)
