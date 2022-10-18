import imp
from django.urls import path
from . import views
urlpatterns = [
    path('meetups/', views.index), #should be active
    path('meetups/<slug:meetup_slug>/', views.meetup_details, name='meetup_detail') #should be active
]