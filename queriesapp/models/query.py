from django.db import models
from .book import Book
from .agent import Agent
from django.contrib.auth.models import User

class Query(models.Model):

    
    notes = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    sent = models.DateField()
    expiration = models.DateField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("query")
        verbose_name_plural = ("queries")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("query_detail", kwargs={"pk": self.pk})