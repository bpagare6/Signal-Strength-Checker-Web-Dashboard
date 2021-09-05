from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.show_dashboard, name="dashboard"),
    path('add-signal-strength', views.add_to_database, name="add-to-database")
]