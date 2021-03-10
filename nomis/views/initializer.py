"""Module that make all the steps"""
from django.http import HttpResponse, JsonResponse

from nomis.views import reports_v
from nomis.views import (
    app_enigne_v,
    cloud_tasks_v,
    datastore_v,
    extract_data_v,
)

def initializer(request):
    """Function that make all the steps for the automatation process"""
    reports.mathops_report(request, input="true")
    cloud_tasks_v.pause(request, id)
    extract_data_v.extract(request)
    datastore_v.setting_range(request)
    cloud_tasks_v.resume(request)

    return HttpResponse("Done!")
