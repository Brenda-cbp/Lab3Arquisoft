from django.urls import path
from . import views

urlpatterns=[
    path('list/',views.get_measurements, name= 'measurementList'),
    path('get/<int:id>/', views.get_measurement, name= 'measurement'), 
    path('delete/<int:id>/', views.delete_measurement, name= 'deleteMeasurement'), 
    path('update/<int:id>/', views.update_measurement, name= 'updateMeasurement'), 
    
]