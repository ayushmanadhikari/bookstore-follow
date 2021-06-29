from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    cover = models.ImageField(upload_to = 'covers/', default='default.jpg', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [('book_detail_accesss', 'can view book details page')]

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.pk)])



class Reviews(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    review = models.CharField(max_length=300)

    def __str__(self):
        return self.review[:20]






