from django.db import models

class ShlongUrl(models.Model):
	short_url = models.CharField(max_length=20)
	long_url = models.URLField(max_length=300)
	shortened = models.DateTimeField(auto_now=False, auto_now_add=True)
