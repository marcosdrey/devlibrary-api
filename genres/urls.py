from django.urls import path
from . import views


urlpatterns = [
    path('', views.GenreListCreateView.as_view(), name='genres_list_create'),
    path('<int:pk>/', views.GenreRetrieveUpdateDestroyView().as_view(), name='genres_rud')
]
