from django.db import models
from students.models import present1

# Create your models here.


class present(models.Model):
    teachers=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    def __str__(self):
        return self.teachers
    


class assighn(models.Model):
   
    teachers=models.ForeignKey(present,on_delete=models.CASCADE, related_name='assignments_teachers')
    names=models.ManyToManyField(present1,blank=True, related_name='assignment_name')
    def __str__(self):
        a = ", ".join(str(student) for student in self.names.all())

        return f"{a}, {self.teachers}"



# class login(models.Model):
#     username=models.CharField(max_length=30)
#     password=models.CharField(max_length=30)
    
