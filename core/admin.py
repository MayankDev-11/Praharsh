from django.contrib import admin
from .models import applicant,Job,JobInfo
from django.contrib import admin

# Register your models here.

class JobInfoAdmin(admin.StackedInline):
    model = JobInfo
    extra = 1

class JobAdmin(admin.ModelAdmin):
    inlines = [JobInfoAdmin]
    list_display = ['designation','location','job_code','pub_date','is_active']
    
    search_fields = ("designation","location",'job_code')
    list_filter = ("location", )


admin.site.register(Job,JobAdmin)
admin.site.register(JobInfo)
admin.site.register(applicant)
