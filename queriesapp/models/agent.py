from django.db import models
from django.contrib.auth.models import User

class Agent(models.Model):

    agent_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("agent")
        verbose_name_plural = ("agents")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("agent_detail", kwargs={"pk": self.pk})