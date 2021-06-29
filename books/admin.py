from django.contrib import admin
from django.db.models.base import Model
from .models import Books, Reviews
from django.contrib.admin import TabularInline
from django.contrib.admin import ModelAdmin


class ReviewAdmin(TabularInline):
    model = Reviews
    fields = ['owner', 'book', 'review']


class BookAdmin(ModelAdmin):
    inlines = [ReviewAdmin]
    list_display = ['title', 'author', 'price']

admin.site.register(Books, BookAdmin)
