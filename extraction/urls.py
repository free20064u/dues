from django.contrib import admin
from django.urls import path
from extraction.views import *

urlpatterns = [
    path('import_data_to_db/', import_data_to_db, name="import_data_to_db"),
    # path("admin/", admin.site.urls),
]