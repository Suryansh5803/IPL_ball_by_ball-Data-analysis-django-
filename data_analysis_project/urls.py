# data_analysis_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data_analysis_app.urls')),  # Include your app's URLs here
]
