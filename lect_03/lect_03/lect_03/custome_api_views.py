from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from lect_03.models import User
from lect_03.serializer import UserSerializer


class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized = UserSerializer(users, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)

        return Response(serialized.errors)
