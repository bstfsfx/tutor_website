from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import School, Subject
from django.forms import NumberInput
from django.db import models
from django import forms
from taggit.forms import TagWidget
from django.contrib.admin.widgets import FilteredSelectMultiple

# Register your models here.
# class SchoolAdminForm(forms.ModelForm):
#     professionals = forms.ModelMultipleChoiceField(
#         queryset=Subject.objects.all(),
#         widget=FilteredSelectMultiple(verbose_name='Professionals', is_stacked=False,
#         attrs={'rows':'5'}), required=False, label='Select Professionals'
#     )

class Meta:
    models = School
    fields = [
            'tutor', 'title', 'address', 'district','description',
            'services', 'service', 'room_type','screen',
            'professionals','professional','rooms',
            'photo_main','photo_1','photo_2','photo_3',
            'photo_4','photo_5','photo_6','is_published',
        ]
    widgets = {
        'services': TagWidget(), # Use Taggit's widget for tags
    }

class SchoolAdmin(admin.ModelAdmin):
    #form = SchoolAdminForm
        list_display = ('id','title','district','is_published')
        list_display_links = ('id','title')
        #list_filter = ("tutor",'services')
        list_editable = ("is_published",)
        search_fields = ('title','district','tutor__name','services__name','professionals__name')
        list_per_page = 25
        ordering=['-id']
    # prepopulated_fields = {'title': ('title',)}
        formfield_overrides = {
        models.IntegerField: {
            'widget': NumberInput (attrs={'size':'10'})
        },
        }
        show_facets = admin.ShowFacets.ALWAYS

def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('services', 'professionals')
    
def display_professionals(self, obj):
        return ", ".join([subject.name for subject in obj.professionals.all()]) or 'None'
display_professionals.short_description = "Professionals"
    
class SubjectAdmin(admin.ModelAdmin):
    list_display = 'name',
    search_fields = ("name",)

admin.site.register(School, SchoolAdmin)
admin.site.register(Subject,SubjectAdmin)