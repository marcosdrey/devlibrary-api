from django.urls import path
from . import views


urlpatterns = [
    path('', views.SubgenreListCreateView.as_view(), name='subgenre-list-create'),
    path('<int:pk>/', views.SubgenreRetrieveUpdateDestroyView.as_view(), name='subgenre-rud')
]
