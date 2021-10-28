from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('wallet.urls',namespace='wallet')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
]


