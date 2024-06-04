from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['GET','PUT'])
def profile(request, user_id):
    user = get_user_model().objects.get(pk=user_id)
    if request.method == 'GET':
        seriazlier = UserSerializer(user)
        return Response(seriazlier.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        if user != request.user:
            return Response({'message': 'disallowed'})
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)