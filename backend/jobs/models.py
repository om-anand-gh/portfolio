import uuid
from django.db import models

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        if self.code:
            return f"{self.code}"
        return self.name


class Province(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="provinces"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "country"], name="unique_location_province_country"
            )
        ]

    def __str__(self):
        if self.code:
            return f"{self.code}"
        return f"{self.name}"


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    city = models.CharField(max_length=255, null=False)
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, related_name="locations"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["city", "province"], name="unique_location_city_province"
            )
        ]

    def __str__(self):
        return f"{self.city}, {self.province}"


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False)
    website = models.CharField(max_length=255, unique=True, null=True)
    about = models.TextField(blank=True, null=True)
    values = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

class JobManager(models.Manager):
    def is_duplicate(self, title, company, locations, exclude_id=None):
        qs = self.filter(title=title, company=company)
        if exclude_id:
            qs = qs.exclude(id=exclude_id)

        for job in qs:
            if set(job.locations.all()) == set(locations):
                return True
        return False
    
class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    locations = models.ManyToManyField(Location)
    title = models.CharField(max_length=255, null=False)
    qualifications = models.TextField(null=True)
    responsibilities = models.TextField(null=True)
    preferred_qualifications = models.TextField(null=True)
    posted_date = models.DateField(null=False)

    objects = JobManager()

    def __str__(self):
        job_str = f"{self.title}, {self.company}"
        for location in set(self.locations.all()):
            job_str += f" | {location}"
        return job_str

    
class JobPostingSite(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return str(self.name)


class JobPostingLink(models.Model):
    STATUS_CHOICES = [
        ("applied", "Applied"),
        ("redirect", "Redirect"),
        ("in_progress", "In Progress"),
        ("not_applicable", "Not Applicable"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    url = models.CharField(max_length=4096, unique=True, null=False)
    job_posting_site = models.ForeignKey(JobPostingSite, on_delete=models.CASCADE)
    html_page = models.FileField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.job}, {self.job_posting_site}"


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    job = models.OneToOneField(Job, models.PROTECT)
    applied_date = models.DateField()

    def __str__(self):
        job = self.job
        return f"{job}, {job.company}"
