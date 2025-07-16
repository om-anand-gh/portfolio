from django.db import models

from jobs.models import Application

class Code(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
    application = models.OneToOneField(Application, on_delete=models.CASCADE, null=True)


class ExperienceGroup(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
