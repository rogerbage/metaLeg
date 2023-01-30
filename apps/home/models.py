# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Decreto(models.Model):
	lei = models.TextField()
	leiClean = models.TextField()
	ano = models.IntegerField()
	ementa = models.TextField()
	ementaClean = models.TextField()
	inteiroTeor = models.TextField()
	inteiroTeorClean = models.TextField()

class LeiOrdinaria(models.Model):
	lei = models.TextField()
	leiClean = models.TextField()
	ano = models.IntegerField()
	ementa = models.TextField()
	ementaClean = models.TextField()
	inteiroTeor = models.TextField()
	inteiroTeorClean = models.TextField()
