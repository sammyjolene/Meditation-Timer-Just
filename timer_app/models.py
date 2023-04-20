from django.db import models

# Create your models here.
class Timer(models.Model):
    meditation_length = models.IntegerField(max_length=3, default=15)
    interval_length = models.IntegerField(max_length=3, default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.meditation_length} minute meditation with {self.interval_length} minute interval bells"