# from django.contrib.auth import authenticate
# from rest_framework.decorators import authentication_classes, permission_classes
# from app.users.permissions import IsAuthenticatedOrCreate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# from django.contrib.contenttypes.management import update_all_contenttypes
from rest_framework.response import Response
from django.http import Http404
from app.order.serializers import OrderSerializer
# from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from app.order.models import Order
# from django.contrib.auth.models import User

class OrderView(APIView):
	
	def post(self,request):
		try:
			order_data = OrderSerializer(data=request.data)
			if not(order_data.is_valid()):
				return Response(order_data.errors)
			order_data.save()
			return Response("order placed successfully",status=status.HTTP_201_CREATED)
		except Exception as err:
			print(err)
			return Response("Error while placing order")

	def get(self,request,order_id=None):
		try:
			if(order_id):
				order_data = Order.objects.filter(pk=order_id,is_deleted = False)[0]
				get_data = OrderSerializer(order_data)
			else:
				order_data = Order.objects.filter(is_deleted = False)
				get_data = OrderSerializer(order_data,many=True)
			return Response(get_data.data,status=status.HTTP_200_OK)
		except Exception as err: 
			print(err) 
			return Response("Error")

	def put(self,request,order_id):
		try:
			get_data = Order.objects.get(pk=order_id)
			update_data = OrderSerializer(get_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return Response("order details updated Successfully")
			else:
				return Response(update_data.errors)	
		except:
			return Response("Error")

	def delete(self,request,order_id):
		try:
			Order.objects.filter(pk=order_id).update(is_deleted = True)
			return Response("order Deleted Successfully",status=status.HTTP_200_OK)
		except Exception as err:
			print(err)    
			return Response("Error while deleting the order",500)


# class LeftItem(APIView):
	
# 	def post(self,request):
# 		try:
# 			LeftItem_data = LeftItemSerializer(data=request.data)
# 			if not(leftitem_data.is_valid()):
# 				return Response(leftitem_data.errors)
# 			LeftItem_data.save()
# 			return Response("leftitem are this much",status=status.HTTP_201_CREATED)
# 		except Exception as err:
# 			print(err)
# 			return Response("Error while geting leftitem")

# 	def get(self,request,leftitem_id=None):
# 		try:
# 			if(leftitem_id):
# 				leftitem_data = Order.objects.filter(pk=leftitem_id,is_deleted = False)[0]
# 				get_data = LeftItemSerializer(leftitem_data)
# 			else:
# 				leftitem_data = Order.objects.filter(is_deleted = False)
# 				get_data = LeftItemSerializer(leftitem_data,many=True)
# 			return Response(get_data.data,status=status.HTTP_200_OK)
# 		except Exception as err: 
# 			print(err) 
# 			return Response("Error")
