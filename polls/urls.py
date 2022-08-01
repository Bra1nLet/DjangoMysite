
from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.register, name='register'),
    path('authorization/', views.auth, name='login'),
    path('Mycabinet/', views.Mycabinet, name='mycabinet')
]