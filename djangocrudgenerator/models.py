# -*- coding: utf-8 -*-

from django.db import models


#test model
class DjangoCRUDGeneratorTestModel(models.Model):
    name = models.CharField(max_length=255)
