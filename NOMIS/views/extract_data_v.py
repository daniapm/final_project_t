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
    extr = extract_data(request.file)
    # acá sí se crea el tax
    taxengine_id = Taxengine()
    taxengine_id.save()
    step = Step.objects.get(code_name="GEN_DUMP")

    if extr:
        report = "extracted data"
        kind = "SUCCES"
        reports = Report(taxengine_id=taxengine_id.id,
                    step_id=step.id, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=200)
    else:
        report = "error extracting data"
        kind = "ERROR"
        reports = Report(taxengine_id=taxengine_id.id,
            step_id=step.id, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=500)
