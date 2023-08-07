from django.contrib import admin

from location.models import *

# Register your models here.
class DisplayCountry(admin.ModelAdmin):
	list_display=('code','name_country','shortcode_country','pub_date','status')
	search_fields=('code','name_country','shortcode_country',)

class DisplayDepartment(admin.ModelAdmin):
	list_display=('code','name_department','shortcode_department','country_fk','pub_date','status')
	search_fields=('code','name_department','shortcode_department',)

class DisplayCity(admin.ModelAdmin):
	list_display=('code','name_city','shortcode_city','department_fk','pub_date','status')
	search_fields=('code','name_city','shortcode_city',)

admin.site.register(Country,DisplayCountry)
admin.site.register(Department,DisplayDepartment)
admin.site.register(City,DisplayCity)

