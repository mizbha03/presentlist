from django.contrib import admin
from teacher.models import present
from teacher.models import assighn

# Register your models here.
class teacherregadmin(admin.ModelAdmin):
    list_display=('teachers','department')

class assighnteacher(admin.ModelAdmin):
    filter_horizontal=['names']

    list_display=['teachers','stud_names']
    def stud_names(self,obj):
        return ", ".join(str(student) for student in obj.names.all())

admin.site.register(present,teacherregadmin)
admin.site.register(assighn,assighnteacher)

