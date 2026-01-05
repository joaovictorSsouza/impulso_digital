from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeViews, name='Employee'),
    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
]