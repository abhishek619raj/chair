from django.db import models
from datetime import datetime


class Login(models.Model):
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)	
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)


