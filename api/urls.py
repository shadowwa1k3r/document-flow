from django.urls import path, include

urlpatterns = [
    path('document/', include('api.documents.urls')),
    path('user/', include('api.users.urls')),
]
