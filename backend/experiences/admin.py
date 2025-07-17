from django.contrib import admin
from .models import Code, Experience, Project, Keyword, Organization

admin.site.register([Code, Experience, Project, Keyword, Organization])
