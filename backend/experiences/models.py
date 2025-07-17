import uuid
from django.db import models

from chats.models import Session
from jobs.models import Application


class Keyword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class ExperienceGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    experience_group = models.ForeignKey(ExperienceGroup, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword)


class Code(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
    application = models.OneToOneField(Application, on_delete=models.PROTECT, null=True)
    experience_groups = models.ManyToManyField(ExperienceGroup)
    chat = models.OneToOneField(Session, on_delete=models.PROTECT)
