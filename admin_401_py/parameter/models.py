from tabnanny import verbose
from django.db import models
from django.db import models
from django.utils.html import format_html
import uuid

STATUS_CHOICES = (
    ('active','Active'),
    ('disabled', 'Disabled'),
)
class BaseModel(models.Model):
    code = models.UUIDField(
         primary_key = False,
         default = uuid.uuid4,
         editable = False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="active")

    class Meta:
        abstract = True


class TypeParameter(BaseModel):
    name_type = models.CharField(max_length=200)

    class Meta:
        verbose_name='Type parameter'
        verbose_name_plural='Types parameters'

    def __str__(self):
        return u"%s" %(self.name_type)

class Parameter(BaseModel):
    name_parameter = models.CharField(max_length=500)
    type_parameter_fk = models.ForeignKey(TypeParameter,on_delete=models.CASCADE, blank=True,null=True, verbose_name='Tipo parametro')

    class Meta:
        verbose_name='Parameter'
        verbose_name_plural='Parameters'

    def __str__(self):
        return u"%s" %(self.name_parameter)


class ParameterDetail(BaseModel):
    value_parameter = models.CharField(max_length=5000)
    parameter_fk = models.ForeignKey(Parameter,on_delete=models.CASCADE, blank=True,null=True, verbose_name='Parametro')

    class Meta:
        verbose_name='Parameter Detail'
        verbose_name_plural='Parameters Details'

    def __str__(self):
        return u"%s" %(self.value_parameter)



