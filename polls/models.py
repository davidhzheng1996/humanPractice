from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Analysis(models.Model):
	stopword = models.BooleanField(default=False)
	words = ArrayField(models.TextField(null=False, default=''),size=25)
	timestamp = models.DateTimeField(auto_now_add=False, null = True, blank = True)
	text = models.TextField(null=False, default='')
