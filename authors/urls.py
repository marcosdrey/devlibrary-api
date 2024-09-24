from django.urls import path
from . import views


urlpatterns = [
    path('', views.AuthorListCreateView.as_view(), name='author_list_create'),
    path('<int:pk>/', views.AuthorRetrieveUpdateDestroyView.as_view(), name='author_rud')
]
