from django.shortcuts import render
from django.views.generic import ListView, DetailView
from books.models import Books, Reviews
from django.contrib.auth import get_user_model


class BookListView(ListView):
    '''Displays the list of available books in the DB
        accessed by url pages/books/ url'''
    model = Books
    template_name = 'book_list.html'
    context_object_name = 'book_lists'


class BookDetailView(DetailView):
    '''displays the details of the selected book
    '''
    model = Books
    template_name = 'book_detail.html'
    context_object_name = 'book'


class UserReviewsList(ListView):
    '''displays the list of reviews done by a particular user'''
    model = Reviews
    template_name = 'user_review_list.html'
    context_object_name = 'user_reviews'

    def get_queryset(self):
        user = self.kwargs.get('user')                    #this captures the user instance from the url
        user = get_user_model().objects.filter(username=user)
        return super().get_queryset().filter(owner=user)