from django.db import models

# Create your models here.

class CollectData(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    # def __str__(self):
    #     return self.name

