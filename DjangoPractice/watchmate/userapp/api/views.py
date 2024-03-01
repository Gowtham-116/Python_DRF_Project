from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from userapp.api.serializers import RegSerializer


@api_view(['POST',])
def logout_view(request):
    
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def reg_view(request):
    if request.method=='POST':
        serializer=RegSerializer(data=request.data)
        
        data={}
        
        if serializer.is_valid():
            account=serializer.save()# when we call this save method, it willexecute save method in serializer and return account
            data['response']="Registration successful"
            data['username']=account.username
            data['email']=account.email 
            
            token=Token.objects.get(user=account).key
            data['token']=token
        else:
            data=serializer.errors
        return Response(data)
