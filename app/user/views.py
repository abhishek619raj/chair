from rest_framework.views import APIView
from rest_framework import status
from app.user.serializers import UserSerializer,LoginSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


class UserCreate(APIView): 
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            userhere = User.objects.get(username=username)
            print(userhere.id)
            idhere = userhere.id
            print(userhere.password)
            print(userhere.last_login)
            print(userhere.is_superuser)
            print(userhere.first_name)
            print(userhere.last_name)
            print(userhere.email)
            print(userhere.is_staff)
            print(userhere.is_active)
            print(userhere.date_joined)
            #from authotoken_token take token of userid of above
            if (userhere):
                    token = Token.objects.get(user_id=user.id)
                    print(token)
                    return Response('login sucess')

            return Response("You are now Logged in.")
        else:
            return Response("You are Not authorized.")


    # def get_queryset(self):
    #     return User.objects.filter(id=self.request.user.id)


