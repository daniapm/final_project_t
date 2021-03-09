from django.contrib import admin

# Register your models here.
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step
from nomis.models.report import Report

admin.site.register(Taxengine)
admin.site.register(Step)
admin.site.register(Report)
