from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Application, Company, Location, Province, Country, Job, JobPostingLink, JobPostingSite

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        company = cleaned_data.get("company")
        locations = cleaned_data.get("locations")  # This works — it's populated here

        if title and company and locations:
            exclude_id = self.instance.pk if self.instance else None
            if Job.objects.is_duplicate(title, company, locations, exclude_id=exclude_id):
                raise ValidationError("A job with this title, company, and the same set of locations already exists.")

        return cleaned_data


class JobPostingLinkInline(admin.TabularInline):
    model = JobPostingLink
    extra = 1

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    form = JobForm
    inlines = [JobPostingLinkInline]
    
admin.site.register([Application, Company, Location, Province, Country, JobPostingLink, JobPostingSite])