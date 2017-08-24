# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tenant_schemas.models import TenantMixin

# Create your models here.

class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until = models.DateField()
    on_trail = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema =True
    
class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.IntegerField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        permissions = (('can_update_authors','Can manipulate authors table'), ('can_get_authors','Can get authors list'))