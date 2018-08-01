from rest_framework import serializers
from app.order.models import Order
from app.chair.models import ChairType,Chair
from app.parts.models import PartType,Part


# class OrderSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model =  Order
# 		fields = ('id','chair','quantity','is_deleted','created_at','updated_at')
# 		extra_kwargs = {
# 			'quantity': {
# 				'required':True,
# 				'error_messages':{
# 				'required':"Please fill this field",
# 				}
# 			}
# 		}

class OrderSerializer(serializers.ModelSerializer):
	# part_type = serializers.SerializerMethodField("getPartTypeName")
	# def getPartTypeName(self,obj):
	# 	try:
	# 		return PartType.objects.get(id=obj.part_type.id).Part
	# 	except Exception as e:
	# 		print(e)
	
	# chair_name = serializers.SerializerMethodField("getChairName")
	# def getChairName(self,obj):
	# 	try:
	# 		return Chair.objects.get(id=obj.chair.id).name
	# 	except Exception as e:
	# 		print(e)

	part_type_name = serializers.SerializerMethodField("getPartTypeName")
	def getPartTypeName(self,obj):
		try:
			return PartType.objects.get(id=obj.parttype.id).name
		except Exception as e:
			print(e)

	chair_name = serializers.SerializerMethodField("getChairName")
	def getChairName(self,obj):
		try:
			return Chair.objects.get(id=obj.chair.id).name
		except Exception as e:
			print(e)

	class Meta:
		model =  Order
		fields = ('id','chair','price','part_type','chair_name','part_type_name','quantity','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'chair': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}


# class LeftItemSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model =  LeftItem
# 		fields = ('id','itemleft','description','is_deleted','created_at','updated_at')
# 		extra_kwargs = {
# 			'item': {
# 				'required':True,
# 				'error_messages':{
# 				'required':"Please fill this item",
# 				}
# 			}
# 		}
# 		