from django.contrib import admin

# Register your models here.
from .models import Backend, Job
admin.site.register(Backend)
admin.site.register(Job)