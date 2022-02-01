from django.urls import path

from landing.views import homepage

urlpatterns = [
    path('', homepage, name='homepage')
]