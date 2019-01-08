# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_at = models.DateField(default=datetime.now, blank=True)
    completed = models.IntegerField(max_length=1, default=0)
    def __str__(self):
        return self.title