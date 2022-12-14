from django.contrib import admin

from .models import CV, Job


class JobAdmin(admin.ModelAdmin):
    list_display = ['name']


class CVAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Job, JobAdmin)
admin.site.register(CV, CVAdmin)