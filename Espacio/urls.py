from django.urls import path
from .views import EspaciosLCAPIView,EspaciosRUDAPIView

app_name = 'Espacio'

urlpatterns =[
    path('',EspaciosLCAPIView.as_view(),name='LC'),
    path('<int:pk>/',EspaciosRUDAPIView.as_view(),name='RUD'),

]