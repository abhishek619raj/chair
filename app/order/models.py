from django.db import models
from datetime import datetime
from app.chair.models import Chair,ChairType
from app.parts.models import Part,PartType


class Order(models.Model):

	chair = models.ForeignKey(Chair)
	# chairtype = models.ForeignKey(ChairType)
	# part = models.ForeignKey(Part)
	parttype = models.ForeignKey(PartType,null=True,blank=True)
	# quantity_of_item = models.IntegerField(blank=True,null=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)