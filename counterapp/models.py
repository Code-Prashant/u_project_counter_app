from django.db import models

class CounterModel(models.Model):
	number = models.CharField(max_length = 10)