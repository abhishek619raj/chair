from django.db import models
from datetime import datetime
from app.chair.models import ChairType

class Part(models.Model):
	name = models.CharField(max_length=500)
	chairtype = models.ForeignKey(ChairType)
	description = models.CharField(max_length=255)	
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

class PartType(models.Model):
	name = models.CharField(max_length=500)
	part = models.ForeignKey(Part)
	description = models.CharField(max_length=255)	
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)	


