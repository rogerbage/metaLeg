# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Decreto(models.Model):
	id = models.BigAutoField(primary_key=True)
	lei = models.TextField(256)
	ano = models.IntegerField()
	ementa = models.TextField()
	inteiroTeor = models.TextField()

class LeiOrdinaria(models.Model):
	id = models.BigAutoField(primary_key=True)
	lei = models.TextField()
	ano = models.IntegerField()
	ementa = models.TextField()
	inteiroTeor = models.TextField()
