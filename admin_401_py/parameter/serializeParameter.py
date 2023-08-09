from rest_framework import serializers
from .models import Parameter
 
class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Parameter
        fields=('name_parameter','application_fk','type_parameter_fk')