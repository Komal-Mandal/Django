from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=100)
    roll = models.IntegerField()

    def __Str__ (self):
        return self.name