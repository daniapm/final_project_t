""" Report model
"""
from django.db import models
from nomis.models.base_model import BaseModel
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step


class Report(BaseModel):
    """Report table for nomis database
    """

    taxengine_id = models.ForeignKey(Taxengine, on_delete=models.CASCADE)
    step_id = models.ForeignKey(Step, on_delete=models.CASCADE)
    message = models.TextField(max_length=100)
    kind = models.CharField(max_length=60)

    def __str__(self):
        return self.message + '-' + self.kind
