from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from app.user.models import Login

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Login 
        fields = ('id','email','password','is_deleted','created_at','updated_at')
        extra_kwargs = {
            'email': {
                'required':True,
                'error_messages':{
                'required':"Please fill this field",
                }
            }
        }

