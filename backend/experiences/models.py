import uuid
from django.db import models

from chats.models import Session
from jobs.models import Application


class Keyword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False)

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False)

class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword)
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)
    content = models.TextField()

class Code(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
    application = models.OneToOneField(Application, on_delete=models.PROTECT, null=True)
    projects = models.ManyToManyField(Project)
    chat = models.OneToOneField(Session, on_delete=models.PROTECT)
    code = models.CharField(max_length=100, unique=True, null=False)
