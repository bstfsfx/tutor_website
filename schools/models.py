from django.db import models
from datetime import datetime


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class School(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=50)
    room_num = models.IntegerField(default=0)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    office_hr = models.CharField(max_length=200)

    # class Meta:
    #     ordering = ('-title',)
    #     indexes = [models.Index(fields=['list_date'])]

    def __str__(self):
        return self.title
    
    # def tag_list(self):
    #     return u", ".join(tag.name for tag in self.services.all())
