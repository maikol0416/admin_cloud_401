from django.db import models
from django.db import models
import uuid
from baseModel.baseEntity import BaseModelShared
from person.models import Person


# Create your models here.
class Application(BaseModelShared):
    name_application = models.CharField(max_length=200)
    description_application = models.CharField(max_length=200)
    url_back_application = models.CharField(max_length=1000)
    url_front_application = models.CharField(max_length=1000)
    technologies_application = models.CharField(max_length=1000)
    person_fk = models.ForeignKey(Person,on_delete=models.CASCADE,blank=True,null=False,verbose_name="Client")

    class Meta:
        verbose_name='Application'
        verbose_name_plural='Applications'

    def __str__(self):
        return u"%s" %(self.name_application)