from django.contrib import admin

from application.models import Application

# Register your models here.

class DisplayApplication(admin.ModelAdmin):
	list_display=('code','name_application','description_application','url_back_application','url_front_application','technologies_application','person_fk','pub_date','status')
	search_fields=('code','name_application','person_fk',)

admin.site.register(Application,DisplayApplication)
