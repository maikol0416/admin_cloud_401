from django.db import models

from baseModel.baseEntity import BaseModelShared

# Create your models here.
class Country(BaseModelShared):
    name_country = models.CharField(max_length=200)
    shortcode_country = models.CharField(max_length=10)
    
    class Meta:
        verbose_name='Country'
        verbose_name_plural='Countries'

    def __str__(self):
        return u"%s" %(self.name_country)


class Department(BaseModelShared):
    name_department = models.CharField(max_length=200)
    shortcode_department = models.CharField(max_length=10)
    country_fk = models.ForeignKey(Country,on_delete=models.CASCADE, blank=True,null=True, verbose_name='Country')

    class Meta:
        verbose_name='Department'
        verbose_name_plural='Departments'

    def __str__(self):
        return u"%s" %(self.name_department)

class City(BaseModelShared):
    name_city = models.CharField(max_length=200)
    shortcode_city = models.CharField(max_length=10)
    department_fk = models.ForeignKey(Department,on_delete=models.CASCADE, blank=True,null=True, verbose_name='Department')

    class Meta:
        verbose_name='City'
        verbose_name_plural='Cities'

    def __str__(self):
        return u"%s" %(self.name_city)

