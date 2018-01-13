from django.db import models
from django.utils import timezone


class PosttoMainPage(models.Model):
    koncertcim = models.CharField(max_length=200)
    helyszin = models.CharField(max_length=200)
    idopont = models.DateTimeField(
            blank=True, null=True)

    def publish(self):

        self.save()

    def __str__(self):
        return self.koncertcim