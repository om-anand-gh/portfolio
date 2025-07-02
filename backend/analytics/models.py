from django.db import models


class VisitCounter(models.Model):
    slug = models.CharField(max_length=255, unique=True, default="homepage")
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.slug}: {self.count}"
