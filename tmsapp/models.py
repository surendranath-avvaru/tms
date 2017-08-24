# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title