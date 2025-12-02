from django.urls import path
from . import views

app_name = 'portafolio_app'

urlpatterns = [
    path('', views.index, name='index'),
]