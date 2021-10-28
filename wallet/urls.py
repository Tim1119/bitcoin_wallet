from django.urls import path
from .views import HomeView,IndexView

app_name='wallet'

urlpatterns = [
    path('home/',HomeView,name='logged-in-home'),
    path('',IndexView.as_view(),name='welcome-home'),
]
