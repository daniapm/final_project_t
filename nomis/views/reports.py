"""Mahops Reports"""
from django.http import HttpResponse, JsonResponse

from nomis.models.report import Report
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step


def mathops_report(request, input, tax_id):
    if input == "true":
        report = "No errors found"
        kind = "SUCCES"
    else:
        report = "Error in mathops"
        kind = "ERROR"

    step = Step.objects.get(code_name="GEN_MATHOPS")
    reports = Report(taxengine_id=Taxengine((str(tax_id))),
                     step_id=Step(str(step.id)), message=report, kind=kind)
    reports.save()
    return HttpResponse(report)
