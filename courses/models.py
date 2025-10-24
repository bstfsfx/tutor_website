from django.db import models
from tutors.models import Tutor  # adjust path if needed

class Course(models.Model):
    CLASS_TYPE_CHOICES = [
        ('live', 'Live'),
        ('video', 'Video'),
    ]

    title = models.CharField(
        max_length=200,
        help_text='Name of the course'
    )
    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE,
        related_name='courses',
        help_text='Tutor teaching this course'
    )
    students_enrolled = models.PositiveIntegerField(
        default=0,
        help_text='Current number of students enrolled'
    )
    max_students = models.PositiveIntegerField(
        default=20,
        help_text='Maximum number of students allowed'
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0,
        help_text='Average rating from 0.0 to 5.0'
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text='Course price in HKD'
    )
    duration_weeks = models.PositiveIntegerField(
        default=1,
        help_text='Course duration in weeks'
    )
    total_classes = models.PositiveIntegerField(
        default=1,
        help_text='Total number of classes in the course'
    )
    class_time = models.CharField(
        max_length=50,
        help_text='Scheduled time for the class (e.g., Wed 4 p.m.)'
    )
    class_type = models.CharField(
        max_length=5,
        choices=CLASS_TYPE_CHOICES,
        default='live',
        help_text='Delivery format of the course'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title

    def enrollment_display(self):
        return f"{self.students_enrolled}/{self.max_students}"