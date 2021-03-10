"""Module with the views for app engine in nomis application
"""

from django.http import HttpResponse, JsonResponse


from nomis.services.app_engine import delete_instances
from nomis.models.report import Report
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step


def delete(request, tax_id):
    """Method to delete instances in google cloud app engine
    """
    dele = delete_instances()
    step = Step.objects.get(code_name="DEL_INSTANCE")
    if dele is True:
        report = "deleted instance"
        kind = "SUCCES"
        reports = Report(taxengine_id=Taxengine((str(tax_id))),
                    step_id=Step(str(step.id)), message=report, kind=kind)
        reports.save()
        return HttpResponse(status=200)
    else:
        report = "error deleting"
        kind = "ERROR"
        reports = Report(taxengine_id=Taxengine((str(tax_id))),
            step_id=Step(str(step.id)), message=report, kind=kind)
        reports.save()
        return HttpResponse(status=500)
