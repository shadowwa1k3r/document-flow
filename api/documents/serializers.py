from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from documents.models import DocumentModel, DocumentModelFile, Receiver
from django.contrib.auth.models import User


class DocumentCreateSerializer(ModelSerializer):
    class Meta:
        model = DocumentModel
        fields = ()

    def create(self, validated_data):
        request = self.context['request']
        doc = DocumentModel(sender=request.user)
        doc.save()
        for rv in request.data.getlist('receivers'):
            # rec = Receiver.objects.get(user=User.objects.get(id=rv))
            # rec.document = doc
            # rec.save()
            doc.receiver.add(Receiver.objects.get(user=User.objects.get(id=rv)))
            doc.save()
        print(request.FILES.getlist("files"))
        for file in request.FILES.getlist('files'):
            print(file)
            docfile = DocumentModelFile.objects.create(owner=doc, file=file)
            # docfile.file.save(file.name, open(file).read())
            docfile.save()
        return doc


class DocumentFilesSerializer(ModelSerializer):
    class Meta:
        model = DocumentModelFile
        fields = ('file',)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ReceiverSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Receiver
        fields = ('user',)


class DocumentSentSerializer(ModelSerializer):
    files = DocumentFilesSerializer(many=True)
    receiver = ReceiverSerializer(many=True)
    sender = UserSerializer()

    class Meta:
        model = DocumentModel
        fields = ('sender', 'created', 'modified', 'files', 'receiver')


class DocumentListSerializer(ModelSerializer):
    files = DocumentFilesSerializer(many=True)
    sender = UserSerializer()

    class Meta:
        model = DocumentModel
        fields = ('sender', 'created', 'modified', 'files')
