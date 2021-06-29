from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from books.models import Books, Reviews
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q


class BookListView(ListView):
    '''Displays the list of available books in the DB
        accessed by url pages/books/ url'''
    model = Books
    template_name = 'book_list.html'
    context_object_name = 'book_lists'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    '''displays the details of the selected book
    '''
    model = Books
    template_name = 'book_detail.html'
    context_object_name = 'book'
    permission_required = ['books.book_detail_accesss']


class UserReviewsList(ListView):
    '''displays the list of reviews done by a particular user'''
    model = Reviews
    template_name = 'user_review_list.html'
    context_object_name = 'user_reviews'

    def get_queryset(self):
        user = get_user_model().objects.filter(username=self.kwargs.get('user')).first()
        qs = Reviews.objects.filter(owner=user)
        return qs


class SearchBookListView(ListView):
    model = Books
    template_name = 'search_page.html'
    context_object_name = 'books'

    def get_queryset(self):
        filter_param = self.request.GET.get('q')
        books = Books.objects.filter(
            Q(title__icontains = filter_param)
        )

        return books