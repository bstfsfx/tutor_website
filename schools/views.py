from django.shortcuts import render, get_object_or_404
from .models import School
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import district_choices, room_choices, rooms_choices
from django.db.models import Q
# Create your views here.
def schools(request):
    #schools = School.objects.all()
    schools = School.objects.order_by('title').filter(is_published=True)
    paginator=Paginator(schools,3)
    page=request.GET.get('page')
    paged_schools=paginator.get_page(page)
    context = {"schools":paged_schools}
    return render(request, 'schools/schools.html',context)

def school(request, school_id):
    school = get_object_or_404(School, pk=school_id)
    context = {"school":school}
    return render(request, 'schools/school.html', context)

def search(request):
    queryset_list = School.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Q(description__icontains=keywords) | Q(title__icontains=keywords) | Q(tutor__name__icontains=keywords))
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district)     
    if 'rooms' in request.GET:
        rooms = request.GET['rooms']
        if rooms:
             queryset_list = queryset_list.filter(rooms__lte=rooms) 
    if 'room_type' in request.GET:
        room_type = request.GET['room_type']
        if room_type:
            
            queryset_list = queryset_list.filter(room_type__iexact=room_type)
    paginator=Paginator(queryset_list,3)
    page=request.GET.get('page')
    paged_schools=paginator.get_page(page)
    
    context = {"schools":paged_schools,
               "district_choices":district_choices,
               "room_choices":room_choices,
               "rooms_choices":rooms_choices,
               "values":request.GET} 
    return render(request, 'schools/search.html', context)
