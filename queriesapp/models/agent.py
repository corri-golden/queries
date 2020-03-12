from django.db import models

class Agent(models.Model):

    agent_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("agent")
        verbose_name_plural = ("agents")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("agent_detail", kwargs={"pk": self.pk})