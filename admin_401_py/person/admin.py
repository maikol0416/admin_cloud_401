from re import search
from django.contrib import admin

# Register your models here.

from .models import *

class DisplayTypeDocument(admin.ModelAdmin):
    list_display=('code','name_type_document','description_type_document','pub_date',)
    search_fields=('code','name_type_document',)

class DisplayTypePerson(admin.ModelAdmin):
    list_display=('code','name_type','description_type','pub_date',)
    search_fields=('code','name_type',)

class DisplayPerson(admin.ModelAdmin):
    list_display=('code','first_name_person','last_name_person','type_document_fk','document_number','phone_number','gender','address','type_person_fk','pub_date',)
    search_fields=('code','first_name_person','document_number',)


admin.site.register(TypeDocument,DisplayTypeDocument)
admin.site.register(TypePerson,DisplayTypePerson)
admin.site.register(Person,DisplayPerson)
