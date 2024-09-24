from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookListCreateView.as_view(), name="book_list_create"),
    path('<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name="book_rud"),
    path('reviews/', views.BookReviewListCreateView.as_view(), name="bookreview_list_create"),
    path('reviews/<int:pk>/', views.BookReviewRetrieveDestroyView.as_view(), name="bookreview_rd"),
    path('reviews/<int:pk>/like/', views.BookReviewUpdateLikeView.as_view(), name="bookreview_like"),
]
