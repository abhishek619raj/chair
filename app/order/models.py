from django.db import models
from datetime import datetime
from app.chair.models import Chair,ChairType
from app.parts.models import Part,PartType


class Order(models.Model):

	chair = models.ForeignKey(Chair)
	part_type = models.ForeignKey(PartType,null=True,blank=True)
	chair_type = models.ForeignKey(ChairType,default="")
	quantity = models.IntegerField(blank=True,null=True)
	price = models.FloatField(null=True, blank=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)