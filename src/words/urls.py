from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('/', views.hello),
    path('home/', views.hello),
]

