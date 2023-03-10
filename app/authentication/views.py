from authentication.models import User
from authentication.serializers import CredentialSerializer, DeleteUserSerializers
from core.utils import Check_User_Token, Delete_User_Token, Find_User, Check_Sql_Injection   
from django.contrib.auth import authenticate,  update_session_auth_hash
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from defense.blacklist import Blacklist


class ProtectedView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def put(self, request):

        if Blacklist(request):
            return Response(status=status.HTTP_403_FORBIDDEN)

        found_user = User.objects.filter(id=request.data['user_id'])

        if not found_user:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(pk=request.data['user_id'])  
        
        if Check_User_Token(request, request.data['user_id']) and user.check_password(request.data['password']):
            try:
                user_new_password = User.objects.get(id=user.id)
                user_new_password.password = make_password(request.data["new_password"])
                user_new_password.save()
                update_session_auth_hash(request, user_new_password)
        
                return Response({"detail": "Password Changed"},status=status.HTTP_200_OK)
            except:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({"detail": "Unauthorized."}, status=status.HTTP_401_UNAUTHORIZED)

    
    def delete(self, request, user_id):

        if Blacklist(request):
            return Response(status=status.HTTP_403_FORBIDDEN)
            
        serializers = DeleteUserSerializers(data=request.data)

        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        if not Find_User(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user = User.objects.get(id=user_id)
        
        if  Check_User_Token(request, user_id) and user.check_password(request.data['password']):
            User.objects.filter(id=user_id).delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
     
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        

class LoginView(APIView): 
    def post(self, request):

        if Blacklist(request) or Check_Sql_Injection(request):
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        serializer = CredentialSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=request.data['email'], password=request.data['password'])

        serializer = CredentialSerializer(user)
 
        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'data': serializer.data, 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, user_id):
        if not Find_User(user_id):
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        Delete_User_Token(user_id)         
        return Response(status=status.HTTP_200_OK)