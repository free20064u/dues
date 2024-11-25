from django.contrib import admin
from django.urls import path
from extraction.views import *

urlpatterns = [
    path('export_data_to_excel/', export_data_to_excel, name="export_data_to_excel"),
    path('import_data_to_db/', import_data_to_db, name="import_data_to_db"),
    # path("admin/", admin.site.urls),
]