from django.contrib import admin
from edoc.models import Projects

# Register your models here.
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'description']

admin.site.register(Projects, ProjectsAdmin)