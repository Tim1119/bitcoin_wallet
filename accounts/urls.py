from django.urls import path
from .views import LoginView,RegisterView,LogoutView

app_name='accounts'

urlpatterns = [
    
    path('register/',RegisterView,name='register'),
    path('login/',LoginView,name='login'),
    path('logout/',LogoutView,name='logout'),
]
