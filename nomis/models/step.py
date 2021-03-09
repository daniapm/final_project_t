""" Step model
"""
from django.db import models
from nomis.models.base_model import BaseModel


class Step(BaseModel):
    """Step table for nomis database
    """
    name = models.TextField(max_length=100, default=None)
    code_name = models.TextField(max_length=100, default=None)

    def __str__(self):
        return self.name
