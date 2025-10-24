from django.urls import path
from . import views

app_name = 'tutors'

urlpatterns = [
    path('', views.tutors, name='tutors'),
    path('<int:tutor_id>/', views.tutor, name='tutor'),
]
