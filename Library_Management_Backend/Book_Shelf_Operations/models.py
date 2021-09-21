from django.db import models
# Create your models here.

class BookShelfModel(models.Model):
    Title      = models.CharField(max_length=100)
    Category   = models.CharField(max_length=100)
    Author     = models.CharField(max_length=100)
    ISBN       = models.CharField(max_length=100)
    Inshelf    = models.BooleanField(default = True)

    def __str__(self):
        return self.title


