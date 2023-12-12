# data_analysis_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_tab, name='data_tab'),  # Handle empty path
    path('descriptive-statistics/', views.descriptive_statistics_tab, name='descriptive_statistics_tab'),
    path('exploratory-data-analysis/', views.exploratory_data_analysis_tab, name='exploratory_data_analysis_tab'),
    path('profile/', views.profile_view, name='profile_view'),
    path('export/csv/', views.export_to_csv, name='export_to_csv'),
    path('export/excel/', views.export_to_excel, name='export_to_excel'),
]
