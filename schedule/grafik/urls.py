from django.contrib import admin
from django.urls import path
from .views import index, add_worker, two

app_name = 'grafik'

urlpatterns = [
    path('', index, name='index'),
    path('addworker', add_worker, name='add_worker'),
    path('asdas', two),
]
