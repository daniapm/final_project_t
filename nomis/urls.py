from django.urls import path
from nomis.views import (
    cloud_tasks,
    app_engine,
    datastore,
    extract_data,
    initializer,
    reports,
)

urlpatterns = [
    path("queues/pause/<str:id>", cloud_tasks.pause),
    path("queues/resume/<str:id>", cloud_tasks.resume),
    path("intances/delete/<str:id>", app_engine.delete),
    path("datastore/updating/<str:id>", datastore.setting_range),
    path("taxengine/extract/", extract_data.extract),
    path("reports/<str:input>/", reports.mathops_report),
    path("init/", initializer.initializer),
]
