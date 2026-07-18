from django.db import models

# Create your models here.
class info(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):  # to show the name of the object instead of object info
        return self.name