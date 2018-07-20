from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class UserProfile(models.Model):

	user = models.ForeignKey(User)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)