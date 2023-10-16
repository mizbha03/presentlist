from django.db import models

# Create your models here.
class present1(models.Model):
    student=models.CharField(max_length=30)
    course=models.CharField(max_length=30)

    def __str__(self):
        return self.student


