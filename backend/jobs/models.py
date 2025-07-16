from django.db import models


class Location(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
    city = models.CharField(max_length=255, unique=True, null=False)
    province = models.CharField(max_length=255, unique=True, null=False)
    country = models.CharField(max_length=255, unique=True, null=False)


class Company(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
    name = models.CharField(max_length=255, unique=True, null=False)
    website = models.CharField(max_length=255, unique=True, null=True)
    about = models.TextField(null=True)
    values = models.TextField(null=True)


class Job(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
    company = models.OneToOneField(Company, on_delete=models.PROTECT)
    locations = models.ManyToManyField(Location)
    url = models.CharField(max_length=4096, unique=True, null=False)
    title = models.CharField(max_length=255, unique=True, null=False)
    qualifications = models.TextField(null=True)
    responsibilities = models.TextField(null=True)
    preferred_qualifications = models.TextField(null=True)
    posted_date = models.DateField(null=False)


class Application(models.Model):
    id = models.UUIDField(primary_key=True, null=False)
    job = models.OneToOneField(Job, models.PROTECT)
    applied_date = models.DateField(null=False)
