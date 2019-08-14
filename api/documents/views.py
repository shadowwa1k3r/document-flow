from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from documents.models import DocumentModel
from api.documents.serializers import DocumentCreateSerializer, DocumentListSerializer,DocumentSentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from  django.db.models import Q

class DocumentCreateAPIView(CreateAPIView):
    serializer_class = DocumentCreateSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = DocumentModel.objects.all()


class DocumentSentListAPIView(ListAPIView):
    serializer_class = DocumentSentSerializer
    queryset = DocumentModel.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        queryset = DocumentModel.objects.filter(sender=self.request.user).filter(~Q(deleted=self.request.user))
        # u_id = self.request.GET.get('u_id')
        # if u_id:
            # queryset = queryset.filter(sender=u_id)
        return queryset


class DocumentReceivedListAPIView(ListAPIView):
    serializer_class = DocumentListSerializer
    queryset = DocumentModel.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        print(DocumentModel.objects.filter(receiver__user=self.request.user).count())
        queryset = DocumentModel.objects.filter(receiver__user=self.request.user).filter(~Q(deleted=self.request.user))
        # u_id = self.request.GET.get('u_id')
        # if u_id:
            # queryset = queryset.filter(sender=u_id)
        return queryset

class DocumentDeleteAPIView(APIView):
    def post(self, request):
        d_id = request.POST.get('message_id')
        d = DocumentModel.objects.get(id=d_id)
        d.deleted.add(request.user)
        d.save()