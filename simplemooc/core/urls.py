from django.urls import path
from .views import home, hello, world

urlpatterns = [
    path('', home, name='home'),
    path('hello/', hello, name='hello'),
    path('world/', world, name='world'),
]
