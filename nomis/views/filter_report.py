"""Module to filter the reports
"""
from django.http import HttpResponse, JsonResponse
from nomis.models.report import Report
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step
def filter_reports(request):
    """Function that filter all reports
    """
    report = Report.objects.get(kind)
    