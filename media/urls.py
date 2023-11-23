from django.urls import path
from .views import main, detail

urlpatterns = [
    path('', main, name='main'),
    path('detail/<str:pk>', detail, name='detail')
]