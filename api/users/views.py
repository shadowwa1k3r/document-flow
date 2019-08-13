from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic.base import View
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from api.users.serializers import UserListSerializer, UserCreateSerializer, UserUpdateSerializer
from django.contrib.auth.models import User


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.filter()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (TokenAuthentication,)


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.filter()
    lookup_url_kwarg = 'id'


class UserCheckApiView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        name = request.GET.get('username')
        if User.objects.filter(username__iexact=name).count() > 0:
            return Response({"result": "exist"})
        else:
            return Response({"result": "not exist"})
    # def get(self, request):
    #     name = request.GET.get('q')
    #     print(request.GET)
    #     if User.objects.filter(username=name).count()>0:
    #         return JsonResponse({"result": "not exist"})
    #     else:
    #         return JsonResponse({"result": "exist"})



