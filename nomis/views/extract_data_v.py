"""Module with the views for extract data in nomis application
"""

from django.http import HttpResponse, JsonResponse

from nomis.services.extract_data import extract_data
from nomis.models.report import Report
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step


def extract(request):
    """Method to extract the data as a value from the engine file
    """
    extr = extract_data()
    # acá sí se crea el tax
    taxengine = Taxengine()
    taxengine.save()
    step = Step(id="22eb8642c9a14be8a81cc46be32c741f")

    if extr:
        report = "extracted data"
        kind = "SUCCES"
        reports = Report(taxengine =taxengine,
                    step_id =step, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=200)
    else:
        report = "error extracting data"
        kind = "ERROR"
        reports = Report(taxengine =taxengine,
            step_id =step, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=500)
