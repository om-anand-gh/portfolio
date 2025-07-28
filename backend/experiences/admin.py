from django.contrib import admin

from .models import Code, Experience, Project, Keyword, Organization
from .utils import generate_project_experience


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def save_model(self, request, obj: Project, form, change):

        # Save the object
        super().save_model(request, obj, form, change)

        generate_project_experience(obj)


admin.site.register([Code, Experience, Keyword, Organization])
