from django.urls import path
from api.users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, UserCheckApiView

urlpatterns = [
    # path('create/', DocumentCreateAPIView.as_view(), name='create'),
    path('list/', UserListAPIView.as_view(), name='list'),
    path('create/', UserCreateAPIView.as_view(), name='createuser'),
    path('check', UserCheckApiView.as_view(), name='checkuser'),
    path('update/<int:id>', UserUpdateAPIView.as_view(), name='updateuser'),
]
