from django.contrib import admin
from .models import Message, Session

admin.site.register([Message, Session])
