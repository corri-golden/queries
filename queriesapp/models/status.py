from django.db import models



class Status(models.Model):

    status_name = models.CharField(max_length=50)    

    class Meta:
        verbose_name = ("status")
        verbose_name_plural = ("statuses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("status_detail", kwargs={"pk": self.pk})
