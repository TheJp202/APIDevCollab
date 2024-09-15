from django.urls import path
from .views import EstacionamientosLCAPIView,EstacionamientosRUDAPIView

app_name = 'Estacionamiento'

urlpatterns =[
    path('',EstacionamientosLCAPIView.as_view(),name='LC_est'),
    path('<int:pk>/',EstacionamientosRUDAPIView.as_view(),name='RUD_est'),

]