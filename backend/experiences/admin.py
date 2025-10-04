from django.contrib import admin

from .models import Code, Experience, Project, Keyword, Organization, ExperienceKeyword
from .utils import generate_project_experience, clean_experience_paragraph


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def save_model(self, request, obj: Project, form, change):

        content_changed = "content" in form.changed_data
        cleaned_changed = "cleaned_content" in form.changed_data

        if content_changed:
            obj.cleaned_content = clean_experience_paragraph(obj.content)
            super().save_model(request, obj, form, change)
            generate_project_experience(obj)

        elif cleaned_changed:
            super().save_model(request, obj, form, change)
            generate_project_experience(obj)

        else:
            # Normal save, no extra work
            super().save_model(request, obj, form, change)

class ExperienceKeywordInline(admin.TabularInline):
    model = ExperienceKeyword
    extra = 1

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceKeywordInline]

admin.site.register([Code, Keyword, Organization])
