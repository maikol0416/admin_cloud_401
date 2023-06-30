from django.http import HttpResponse
from .models import Parameter
from django.shortcuts import render
from django.http import Http404


def index(request):
    latest_parameter_list = Parameter.objects.order_by("-pub_date")[:5]
    context = {"latest_parameter_list": latest_parameter_list}
    return render(request, "parameter/index.html", context)

def detail(request, parameter_id):
    try:
        parameter = Parameter.objects.get(pk=parameter_id)
        print(parameter)
    except Parameter.DoesNotExist:
        raise Http404("Parameter does not exist")
    return render(request, "parameter/detail.html", {"parameter": parameter})


def results(request, parameter_id):
    response = "You're looking at the results of parameter %s."
    return HttpResponse(response % parameter_id)


def vote(request, parameter_id):
    return HttpResponse("You're voting on parameter %s." % parameter_id)