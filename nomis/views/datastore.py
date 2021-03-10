"""Module with the views for datastore in nomis application
"""

from django.http import HttpResponse, JsonResponse

from nomis.services.datastore import set_datastore_range
from nomis.models.report import Report
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step


def setting_range(request, tax_id):
    """Method to set entities in google cloud data store
    """
    sett = set_datastore_range()
    # traer el id 
    # cambiar id por code name, crear la columna en la bd
    step = Step.objects.get(code_name="UPDATE_RANGE")

    if sett == "UPDATED":
        report = "updated entitie"
        kind = "SUCCES"
        reports = Report(message=report, kind=kind)
        reports.taxengine_id = tax_id
        reports.step_id = step
        reports.save()
        return HttpResponse(status=200)
    else:
        report = "error updating"
        kind = "ERROR"
        reports = Report(message=report, kind=kind)
        reports.taxengine_id = tax_id
        reports.step_id = step
        reports.save()
        return HttpResponse(status=400)
