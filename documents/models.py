from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class DocumentModel(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ManyToManyField('Receiver', related_name='receiver')
    title = models.TextField(default='')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(DocumentModel, self).save(*args, **kwargs)


class Receiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # document = models.ForeignKey(DocumentModel, on_delete=models.CASCADE, null=True, related_name='receivers')


class DocumentModelFile(models.Model):
    file = models.FileField(upload_to='documents/', null=True)
    owner = models.ForeignKey(DocumentModel, on_delete=models.CASCADE, related_name='files')


@receiver(post_save, sender=User)
def gen_rec(instance, created, **kwargs):
    if created:
        rec = Receiver.objects.create(user=instance)
        rec.save()