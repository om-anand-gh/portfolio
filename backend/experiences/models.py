import uuid
from django.db import models

from utils.models import DefaultVectorField

from chats.models import Session
from jobs.models import Application, Location


class Keyword(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False)
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, null=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    content = models.TextField(default="")

    def __str__(self):
        return f"{self.name}, {self.organization}"


class Experience(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword)
    ordering = models.PositiveIntegerField(default=0)
    content = models.TextField()
    embedding = DefaultVectorField(null=True, default=None)

    def __str__(self):
        return f"{self.project} - {self.ordering} - {self.content}"


class Code(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
    application = models.OneToOneField(Application, on_delete=models.PROTECT, null=True)
    projects = models.ManyToManyField(Project)
    chat = models.OneToOneField(Session, on_delete=models.PROTECT)
    code = models.CharField(max_length=100, unique=True, null=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}, {self.description}"
