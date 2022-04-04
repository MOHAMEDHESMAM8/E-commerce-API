from django.contrib.contenttypes.models import ContentType
from django.db import models


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TagItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    ContentType = models.ForeignKey(ContentType,  on_delete=models.CASCADE)
    object_id= models.PositiveIntegerField()
    content_object= models.GenericForeignKey()