from django.urls import path
from .import views


urlpatterns = [
    path('',views.sey_hello)
]