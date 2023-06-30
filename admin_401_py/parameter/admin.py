from django.contrib import admin

from .models import *

class DisplayTypeParameter(admin.ModelAdmin):
	list_display=('name_type','pub_date')
	search_fields=('name_type',)

class DisplayParameter(admin.ModelAdmin):
	list_display=('name_parameter','type_parameter_fk','pub_date')
	search_fields=('name_parameter',)

class DisplayParameterDetail(admin.ModelAdmin):
	list_display=('value_parameter','parameter_fk')
	search_fields=('value_parameter',)

admin.site.register(TypeParameter,DisplayTypeParameter)
admin.site.register(Parameter,DisplayParameter)
admin.site.register(ParameterDetail,DisplayParameterDetail)
