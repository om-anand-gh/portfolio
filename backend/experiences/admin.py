from django.contrib import admin
from .models import Code, Experience, ExperienceGroup, Keyword

admin.site.register([Code, Experience, ExperienceGroup, Keyword])
