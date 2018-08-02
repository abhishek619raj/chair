# from django.contrib.auth import authenticate
# from rest_framework.decorators import authentication_classes, permission_classes
# from app.users.permissions import IsAuthenticatedOrCreate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from django.contrib.contenttypes.management import update_all_contenttypes
from rest_framework.response import Response
from django.http import Http404
from app.parts.serializers import PartSerializer ,PartTypeSerializer
# from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from app.parts.models import Part ,PartType
# from django.contrib.auth.models import User


class PartView(APIView):
	
	def post(self,request):
		try:
			part_data = PartSerializer(data=request.data)
			if not(part_data.is_valid()):
				return Response(part_data.errors)
			part_data.save()
			print(part_data);
			return Response(part_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error while creating part")

	def get(self,request,part_id=None):
		try:
			if(part_id):
				part_data = Part.objects.filter(pk=part_id,is_deleted = False)[0]
				get_data = PartSerializer(part_data)
			else:
				part_data = Part.objects.filter(is_deleted = False)
				get_data = PartSerializer(part_data,many=True)
			return Response(get_data.data,status=status.HTTP_200_OK)
		except Exception as err: 
			print(err) 
			return Response("Error")


	def put(self,request,part_id):
		try:
			get_data = Part.objects.get(pk=part_id)
			update_data = PartSerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response("Part details updated Successfully")
			else:
				return Response(update_data.errors)	
		except:
			return Response("Error")

	def delete(self,request,part_id):
		try:
			Part.objects.filter(pk=part_id).update(is_deleted = True)
			return Response("Part Deleted Successfully",status=status.HTTP_200_OK)
		except Exception as err:
			print(err)    
			return Response("Error while deleting the Part",500)


class PartTypeView(APIView):
	
	def post(self,request):
		try:
			parttype_data = PartTypeSerializer(data=request.data)
			if not(parttype_data.is_valid()):
				return Response(parttype_data.errors)
			parttype_data.save()
			return Response(parttype_data.data,status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error while creating Parttype")

	def get(self,request,parttype_id=None):
		try:
			if(parttype_id):
				parttype_data = PartType.objects.filter(pk=parttype_id,is_deleted = False)[0]
				get_data = PartTypeSerializer(parttype_data)
			else:
				parttype_data = PartType.objects.filter(is_deleted = False)
				get_data = PartTypeSerializer(parttype_data,many=True)
			return Response(get_data.data,status=status.HTTP_200_OK)
		except Exception as err: 
			print(err) 
			return Response("Error")

	def put(self,request,parttype_id):
		try:
			get_data = PartType.objects.get(pk=parttype_id)
			update_data = PartTypeSerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response("PartType details updated Successfully")
			else:
				return Response(update_data.errors)	
		except:
			return Response("Error")

	def delete(self,request,parttype_id):
		try:
			PartType.objects.filter(pk=parttype_id).update(is_deleted = True)
			return Response("PartType Deleted Successfully",status=status.HTTP_200_OK)
		except Exception as err:
			print(err)    
			return Response("Error while deleting the PartType",500)