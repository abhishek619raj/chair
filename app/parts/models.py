from django.db import models
from datetime import datetime

class Part(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)	
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

class PartType(models.Model):
	name = models.CharField(max_length=255)
	part = models.ForeignKey(Part)
	description = models.CharField(max_length=255)
	quantity_item = models.IntegerField()
	price_item = models.FloatField(null=True,blank=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)