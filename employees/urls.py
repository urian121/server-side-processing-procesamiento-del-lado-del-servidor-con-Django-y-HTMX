from django.urls import path
from . import views 

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('data/', views.employee_data, name='employee_data'),
    path('count/', views.employee_count, name='employee_count'),
]