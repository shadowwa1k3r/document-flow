from django.contrib import admin
from documents.models import DocumentModel, DocumentModelFile, Receiver

admin.site.register(DocumentModel)
admin.site.register(DocumentModelFile)
admin.site.register(Receiver)