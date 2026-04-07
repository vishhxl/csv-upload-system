from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_csv),
    path('data/', views.show_data),
]