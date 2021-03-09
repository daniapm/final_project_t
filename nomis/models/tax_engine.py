""" Tax engine model
"""
from django.db import models
from nomis.models.base_model import BaseModel


class Taxengine(BaseModel):
    """Taxengine table for nomis database
    """
    completed_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=100)
    succes = models.BooleanField(default=False)

    def __str__(self):
        return self.description
