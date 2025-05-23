from django.contrib import admin
from .models import Commission, Job, JobApplication

class CommissionAdmin(admin.ModelAdmin):
    model = Commission

class JobAdmin(admin.ModelAdmin):
    model = Job

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)