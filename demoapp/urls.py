from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.registers, name='registers'),
    path('logi/', views.logins, name='logins'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('homes/', views.home, name='home'),
    
]
