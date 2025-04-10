from django.urls import path
from .views import *

urlpatterns = [
    path('',demo),
    path('order',orderview.as_view())
]