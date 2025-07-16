from django.contrib import admin
from .models import Company, Location, Job, Application

admin.register(Company, Location, Job, Application)