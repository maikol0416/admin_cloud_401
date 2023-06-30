from tabnanny import verbose
from django.db import models
import uuid
from parameter.models import *

GENDER_CHOICES = (
    ('F','Female'),
    ('M', 'Male'),
    ('O', 'Other'),
)

class TypeDocument(BaseModel):
    name_type_document = models.CharField(max_length=100)
    description_type_document = models.CharField(max_length=200)

    class Meta:
        verbose_name='Type document'
        verbose_name_plural='Types document'

    def __str__(self):
        return u"%s" %(self.name_type_document)


class TypePerson(BaseModel):
    name_type= models.CharField(max_length=200)
    description_type= models.CharField(max_length=200)

    class Meta:
        verbose_name='Type person'
        verbose_name_plural='Types person'

    def __str__(self):
        return u"%s" %(self.name_type)

class Person(BaseModel):
    first_name_person = models.CharField(max_length=200)
    last_name_person = models.CharField(max_length=200)
    document_number=models.CharField(max_length=100,null=False)
    phone_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=200,choices=GENDER_CHOICES,default="F")
    address = models.CharField(max_length=100)
    type_person_fk = models.ForeignKey(TypePerson,on_delete=models.CASCADE,blank=True,null=False,verbose_name="Type person")
    type_document_fk = models.ForeignKey(TypeDocument,on_delete=models.CASCADE,blank=True,null=False, verbose_name="Type document")
    
    class Meta:
        verbose_name='Person'
        verbose_name_plural='People'

    def __str__(self):
        return u"%s" %(self.first_name_person)


    
