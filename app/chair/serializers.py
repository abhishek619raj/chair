from rest_framework import serializers
from app.chair.models import Chair,ChairType
from app.parts.models import Part,PartType

class ChairSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Chair 
		fields = ('id','name','description','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'name': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}



class ChairTypeSerializer(serializers.ModelSerializer):
	part_type_name = serializers.SerializerMethodField("getPartTypeName")
	def getPartTypeName(self,obj):
		try:
			return PartType.objects.get(id=obj.part_type.id).name
		except Exception as e:
			print(e)

	chair_name = serializers.SerializerMethodField("getChairName")
	def getChairName(self,obj):
		try:
			return Chair.objects.get(id=obj.chair.id).name
		except Exception as e:
			print(e)
	
	class Meta:
		model =  ChairType
		fields = ('id','part_type','part_type_name','parent_id','chair_name','chair','name','description','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'name': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}

