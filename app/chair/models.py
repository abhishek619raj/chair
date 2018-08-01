from django.db import models
from datetime import datetime
from app.parts.models import PartType

# for single chair like plastic
class Chair(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)	
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)


#  for custom chair 
class ChairType(models.Model):
	name = models.CharField(max_length=255)
	chair = models.ForeignKey(Chair)
	part_type = models.ForeignKey(PartType)
	parent_id = models.IntegerField()
	description = models.CharField(max_length=255)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)