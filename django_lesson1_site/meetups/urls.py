from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups-url'), # our-domain.com/meetups
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail-url'), # our-domain.com/meetups/<a dynamic-path-segment> e.g. a-first-meetup
]