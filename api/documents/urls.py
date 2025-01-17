from django.urls import path
from api.documents.views import DocumentCreateAPIView, DocumentSentListAPIView, DocumentReceivedListAPIView, DocumentDeleteAPIView

urlpatterns = [
    path('create/', DocumentCreateAPIView.as_view(), name='create'),
    path('delete/', DocumentDeleteAPIView.as_view(), name='delete'),
    path('list/sent/', DocumentSentListAPIView.as_view(), name='sent-list'),
    path('list/received/', DocumentReceivedListAPIView.as_view(), name='received-list'),
]
