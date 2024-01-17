from django.contrib import admin
from projects.models import Project
from users.models import CustomUser

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomUser, UserAdmin)

# Register your models here.
