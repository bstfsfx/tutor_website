from django.contrib import admin
from .models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'tutor', 'students_enrolled', 'max_students', 'rating', 'price', 'duration_weeks', 'class_type')
    list_display_links = ('title', )
    list_editable = ('tutor','price', 'duration_weeks', 'class_type', 'students_enrolled')


admin.site.register(Course, CourseAdmin)
