
# from django.shortcuts import render
# from django.http import Http404

# from drf_yasg import openapi
# from drf_yasg.app_settings import swagger_settings
# from drf_yasg.inspectors import DrfAPICompatInspector, FieldInspector, NotHandled, SwaggerAutoSchema
# from drf_yasg.utils import no_body, swagger_auto_schema
# from rest_framework.decorators import action
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status , generics
import json
from django.http import HttpResponse

from parameter.serializeParameter import ParameterSerializer
from .models import Parameter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import no_body, swagger_auto_schema


@api_view(['POST'])
def createParameter(request):
    #did = request.POST.get('codigo')
    # bloodgroup = request.POST.get('bloodgroup')
    # birthmark = request.POST.get('birthmark')
    #print(ParameterSerializer(request.data))
    return Response(request.data, status=status.HTTP_201_CREATED)
    # try:
    #     Parameter.objects.create(name= name, bloodgroup = bloodgroup, birthmark = birthmark)
    #     return Response("Data Saved!", status=status.HTTP_201_CREATED)
    # except Exception as ex:
    #     return Response(ex, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getParameters(request):
    return Response(Parameter.objects.all().values(), status=status.HTTP_200_OK)