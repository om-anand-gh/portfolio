import uuid
from django.db import models


class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    chat_session = models.ForeignKey(Session, on_delete=models.CASCADE)
