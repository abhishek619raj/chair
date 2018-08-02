from rest_framework import serializers
from app.order.models import Order
from app.chair.models import ChairType,Chair
from app.parts.models import PartType,Part



class OrderSerializer(serializers.ModelSerializer):
	
	quantity_data = serializers.SerializerMethodField("getQuantity")
	def getQuantity(self,obj):
		try:
			return PartType.objects.get(id=obj.part_type.id).quantity_item
		except Exception as e:
			print(e)

	chair_parent_id = serializers.SerializerMethodField("ChairParentId")
	def ChairParentId(self,obj):
		try:
			return ChairType.objects.get(id=obj.chair_type.id).parent_id
		except Exception as e:
			print(e)

	class Meta:
		model =  Order
		fields = ('id','chair','price','chair_type','part_type','quantity_data','chair_parent_id','quantity','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'chair': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}
