from rest_framework import serializers
from app.parts.models import Part ,PartType

class PartSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Part 
		fields = ('id','name','description','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'name': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}

		
class PartTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model =  PartType
		fields = ('id','name','part','description','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'name': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}



		
