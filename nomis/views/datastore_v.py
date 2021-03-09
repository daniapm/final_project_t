"""Module with the views for datastore in nomis application
"""

from django.http import HttpResponse, JsonResponse

from nomis.services.datastore import set_datastore_range
from nomis.models.report import Report
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step


def setting_range(request, id):
    """Method to set entities in google cloud data store
    """
    sett = set_datastore_range()
    # traer el id 
    taxengine_id = Taxengine(id=id)
    # cambiar id por code name, crear la columna en la bd
    step = Step(id="c254f9f0c649496bb9da8d09d8f2d672")

    if sett == "UPDATED":
        report = "updated entitie"
        kind = "SUCCES"
        reports = Report(taxengine_id =taxengine_id,
                    step_id =step, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=200)
    else:
        report = "error updating"
        kind = "ERROR"
        reports = Report(taxengine_id =taxengine_id,
                    step_id =step, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=400)
