from django.urls import path
from . import views

urlpatterns = [
    path('', views.PublisherListCreateView.as_view(), name='publisher_list_create'),
    path('<int:pk>/', views.PublisherRetrieveUpdateDestroyView.as_view(), name='publisher-rud')
]
