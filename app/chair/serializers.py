from rest_framework import serializers
from app.chair.models import Chair,ChairType

# from app.user.models import UserProjects

## written by abhishek
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
	class Meta:
		model =  ChairType
		fields = ('id','name','chair','description','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'name': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			}
		}



		
