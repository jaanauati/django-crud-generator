from django.db import models

# Create your models here.

class Modelname(models.Model):
    first_name= models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dni =models.CharField(max_length=20)
    phone_number=models.CharField(max_length=10)
    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

