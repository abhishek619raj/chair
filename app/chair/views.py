# from django.contrib.auth import authenticate
# from rest_framework.decorators import authentication_classes, permission_classes
# from app.users.permissions import IsAuthenticatedOrCreate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from django.contrib.contenttypes.management import update_all_contenttypes
from rest_framework.response import Response
from django.http import Http404
from app.chair.serializers import ChairSerializer,ChairTypeSerializer
# from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from app.chair.models import Chair,ChairType
# from django.contrib.auth.models import User


class ChairView(APIView):
	
	def post(self,request):
		try:
			chair_data = ChairSerializer(data=request.data)
			if not(chair_data.is_valid()):
				return Response(chair_data.errors)
			chair_data.save()
			return Response(chair_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error while creating chair")

	def get(self,request,chair_id=None):
		try:
			if(chair_id):
				chair_data = Chair.objects.filter(pk=chair_id,is_deleted = False)[0]
				get_data = ChairSerializer(chair_data)
			else:
				chair_data = Chair.objects.filter(is_deleted = False)
				get_data = ChairSerializer(chair_data,many=True)
			return Response(get_data.data,status=status.HTTP_200_OK)
		except Exception as err: 
			print(err) 
			return Response("Error")


	def put(self,request,chair_id):
		try:
			get_data = Chair.objects.get(pk=chair_id)
			update_data = ChairSerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response("chair details updated Successfully")
			else:
				return Response(update_data.errors)	
		except:
			return Response("Error")

	def delete(self,request,chair_id):
		try:
			Chair.objects.filter(pk=chair_id).update(is_deleted = True)
			return Response("chair Deleted Successfully",status=status.HTTP_200_OK)
		except Exception as err:
			print(err)    
			return Response("Error while deleting the chair",500)



class ChairTypeView(APIView):
	
	def post(self,request):
		try:
			chairtype_data = ChairTypeSerializer(data=request.data)
			if not(chairtype_data.is_valid()):
				return Response(chairtype_data.errors)
			chairtype_data.save()
			return Response("chairtype created successfully",status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error while creating chairtype")

	def get(self,request,chairtype_id=None):
		try:
			if(chairtype_id):
				chairtype_data = ChairType.objects.filter(pk=chairtype_id,is_deleted = False)[0]
				get_data = ChairTypeSerializer(chairtype_data)
			else:
				chairtype_data = ChairType.objects.filter(is_deleted = False)
				get_data = ChairTypeSerializer(chairtype_data,many=True)
			return Response(get_data.data,status=status.HTTP_200_OK)
		except Exception as err: 
			print(err) 
			return Response("Error")

	def put(self,request,chairtype_id):
		try:
			get_data = ChairType.objects.get(pk=chairtype_id)
			update_data = ChairTypeSerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response("chairtype details updated Successfully")
			else:
				return Response(update_data.errors)	
		except:
			return Response("Error")

	def delete(self,request,chairtype_id):
		try:
			ChairType.objects.filter(pk=chairtype_id).update(is_deleted = True)
			return Response("chairtype Deleted Successfully",status=status.HTTP_200_OK)
		except Exception as err:
			print(err)    
			return Response("Error while deleting the chairtype",500)