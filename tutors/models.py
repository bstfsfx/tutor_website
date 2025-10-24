from django.db import models
from datetime import datetime
# Create your models here.
class Tutor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, default='00000000')
    email = models.EmailField(max_length=50, unique=False, blank=True)
    is_mvp = models.BooleanField(default=True)
    hire_date = models.DateTimeField(auto_now_add=True)
    course_subject = models.CharField(blank=False, default=None)

    def __str__(self):
        return self.name