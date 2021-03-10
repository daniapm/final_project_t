"""Module that make all the steps"""
from django.http import HttpResponse, JsonResponse

from nomis.views import reports
from nomis.views import (
    app_engine,
    cloud_tasks,
    datastore,
    extract_data,
)

def initializer(request):
    """Function that make all the steps for the automatation process"""
    reports.mathops_report(request, input="true")
    cloud_tasks.pause(request, id)
    extract_data.extract(request)
    datastore.setting_range(request)
    cloud_tasks.resume(request)

    return HttpResponse("Done!")
