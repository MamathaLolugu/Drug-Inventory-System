
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_dashboard, name='main_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_drug, name='add_drug'),
    path('movement/', views.movement_history, name='movement_history'),
    path('scan_qr/', views.scan_qr, name='scan_qr'),
    path('scan_qr_page/', views.main_dashboard, name='scan_qr_page'),


]
