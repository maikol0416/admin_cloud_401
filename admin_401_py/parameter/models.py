from tabnanny import verbose
from django.db import models
from application.models import Application
from baseModel.baseEntity import BaseModelShared


class TypeParameter(BaseModelShared):
    name_type = models.CharField(max_length=200)

    class Meta:
        verbose_name='Type parameter'
        verbose_name_plural='Types parameters'

    def __str__(self):
        return u"%s" %(self.name_type)

class Parameter(BaseModelShared):
    name_parameter = models.CharField(max_length=500)
    application_fk = models.ForeignKey(Application,on_delete=models.CASCADE, blank=True,null=True, verbose_name='Application')
    type_parameter_fk = models.ForeignKey(TypeParameter,on_delete=models.CASCADE, blank=True,null=True, verbose_name='Type parameter')

    class Meta:
        verbose_name='Parameter'
        verbose_name_plural='Parameters'

    def __str__(self):
        return u"%s" %(self.name_parameter)


class ParameterDetail(BaseModelShared):
    value_parameter = models.CharField(max_length=5000)
    parameter_fk = models.ForeignKey(Parameter,on_delete=models.CASCADE, blank=True,null=True, verbose_name='Parameter')

    class Meta:
        verbose_name='Parameter Detail'
        verbose_name_plural='Parameters Details'

    def __str__(self):
        return u"%s" %(self.value_parameter)



