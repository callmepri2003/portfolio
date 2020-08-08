from django.db import models

# Create your models here.

class Inquiry(models.Model):
	name = models.CharField(max_length=30)
	phone = models.IntegerField(max_length=12)
	reason = models.TextField(max_length=300)
