"""Module with the views for app engine in nomis application
"""

from django.http import HttpResponse, JsonResponse


from nomis.services.app_engine import delete_instances
from nomis.models.report import Report
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step


def delete(request, id):
    """Method to delete instances in google cloud app engine
    """
    dele = delete_instances()
    taxengine_id = Taxengine(id=id)
    #taxengine_id = Taxengine(id="c5f8ddaf-83c8-416c-b650-bacbc85c7086")
    step = Step(id="a8b9215b78a24a5f9afc4eba744b2ade")
    if dele is True:
        report = "deleted instance"
        kind = "SUCCES"
        reports = Report(taxengine_id =taxengine_id,
                    step_id =step, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=200)
    else:
        report = "error deleting"
        kind = "ERROR"
        reports = Report(taxengine_id =taxengine_id,
            step_id =step, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=500)
