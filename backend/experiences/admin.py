from django.contrib import admin

from .models import Code, Experience, Project, Keyword, Organization, ExperienceKeyword
from .utils import generate_project_experience


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def save_model(self, request, obj: Project, form, change):

        # Save the object
        super().save_model(request, obj, form, change)

        generate_project_experience(obj)


class ExperienceKeywordInline(admin.TabularInline):
    model = ExperienceKeyword
    extra = 1

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceKeywordInline]

admin.site.register([Code, Keyword, Organization])
