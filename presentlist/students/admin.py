from django.contrib import admin
from students.models import present1

# Register your models here.
class studentregadmin(admin.ModelAdmin):
    list_display=('student','course')
admin.site.register(present1,studentregadmin)