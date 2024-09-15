from django.urls import path
from .views import ClienteEspaciosLCAPIView,ClienteEspaciosRUDAPIView,CalcularCobroClienteAPIView

app_name = 'ClienteEspacio'

urlpatterns =[
    path('',ClienteEspaciosLCAPIView.as_view(),name='LC'),
    path('<int:pk>/',ClienteEspaciosRUDAPIView.as_view(),name='RUD'),
    path('<int:pk>/costo/', CalcularCobroClienteAPIView.as_view(), name='costo'),
]