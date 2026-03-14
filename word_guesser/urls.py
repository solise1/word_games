from django.urls import path
from . import views


urlpatterns = [
  path('', views.word_guesser, name='word_guesser'),
  path('guess/', views.guess, name='guess'),
]
