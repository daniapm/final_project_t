from django.urls import path
from nomis.views import (
    cloud_tasks_v,
    app_enigne_v,
    datastore_v,
    extract_data_v,
    initializer_v,
    reports_v,
    # drop_v,
)
urlpatterns = [
    path('queues/pause/<str:id>', cloud_tasks_v.pause),
    path('queues/resume/<str:id>', cloud_tasks_v.resume),
    path('intances/delete/<str:id>', app_enigne_v.delete),
    path('datastore/updating/<str:id>', datastore_v.setting_range),
    path('taxengine/extract/', extract_data_v.extract),
    path('reports/<str:input>/', reports_v.mathops_report),
    path('init/', initializer_v.initializer),
    # path('drop/', drop_v.drop_file),
]
