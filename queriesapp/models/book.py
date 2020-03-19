from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):

    book_name = models.CharField(max_length=50)
    num_of_pages = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("book")
        verbose_name_plural = ("books")

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})