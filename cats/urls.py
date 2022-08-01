
from django.urls import path
from . import views
app_name = 'cats'

urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('main/<int:pk>/update', views.UpdateCat.as_view(), name='cat_update'),
    path('main/create', views.AddCat.as_view(), name='cat_create'),
    path('main/<int:pk>/delete', views.DeleteteCat.as_view(), name='cat_delete'),
    path('lookup/', views.BreedsList.as_view(), name='breed_all'),
    path('lookup/create/', views.AddBreed.as_view(), name='breed_create'),
    path('lookup/<int:pk>/delete', views.DeleteBreed.as_view(), name='breed_delete'),
    path('lookup/<int:pk>/update', views.UpdateBreed.as_view(), name='breed_update'),
]
