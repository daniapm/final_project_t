"""Mahops Reports"""
from django.http import HttpResponse, JsonResponse

from nomis.models.report import Report
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step


def mathops_report(request, input):
    if input == "true":
        report = "No errors found"
        kind = "SUCCES"
    else:
        report = "Error in mathops"
        kind = "ERROR"

    taxengine_id = Taxengine(id="c5f8ddaf-83c8-416c-b650-bacbc85c7086")
    step = Step(id="00a4a89e0d33480fb59971b30ec24ce6")
    reports = Report(taxengine_id =taxengine_id,
                     step_id =step, message=report, kind=kind)
    reports.save()
    return HttpResponse(report)
