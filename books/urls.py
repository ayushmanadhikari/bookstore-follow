from django.urls import path
from .views import BookListView, BookDetailView, UserReviewsList

urlpatterns = [
    path('list/', BookListView.as_view(), name='book-list'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('reviews/<str:user>/', UserReviewsList.as_view(), name="user-review-list"),
]