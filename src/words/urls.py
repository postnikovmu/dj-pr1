from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('home/', views.hello),
    path('words_list/', views.show_words_list),
]

