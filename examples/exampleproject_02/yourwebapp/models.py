from django.db import models

class YourModel(models.Model):
    name=models.CharField(max_length=30)
    serial=models.CharField(max_length=20)
    def __str__(self):
        return self.name

