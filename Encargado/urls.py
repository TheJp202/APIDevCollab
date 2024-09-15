from django.urls import path
from .views import login_view,register_view,logout_view,user_data_cookie_view, change_password

app_name = 'Encargado'

urlpatterns =[
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('logout/',logout_view,name='logout'),
    path('password/',change_password,name='password'),
    path('cookie/',user_data_cookie_view,name='cookie'),

]