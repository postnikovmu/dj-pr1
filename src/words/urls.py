from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.hello),
    path('words_list/', views.show_words_list),
    path('add_word/', views.add_word, name='add_word'),
    path('', views.hello),
]

