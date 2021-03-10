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
    extr = extract_data(request.body)
    print(dir(request))
    # acá sí se crea el tax
    taxengine = Taxengine()
    taxengine.save()
    step = Step.objects.get(code_name="GEN_DUMP")

    if extr:
        report = "extracted data"
        kind = "SUCCES"
        reports = Report(taxengine_id=Taxengine(str(taxengine.id)),
                    step_id=Step(str(step.id)), message=report, kind=kind)
        reports.save()
        return HttpResponse(status=200)
    else:
        report = "error extracting data"
        kind = "ERROR"
        reports = Report(taxengine_id=Taxengine(str(taxengine.id)),
            step_id=Step(str(step.id)), message=report, kind=kind)
        reports.save()
        return HttpResponse(status=500)
