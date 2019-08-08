from django.urls import path
from api.users.views import UserListAPIView, UserCreateAPIView

urlpatterns = [
    # path('create/', DocumentCreateAPIView.as_view(), name='create'),
    path('list/', UserListAPIView.as_view(), name='list'),
    path('createuser/', UserCreateAPIView.as_view(), name='createuser'),
]
