from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from event_api import views


urlpatterns = [
    
    path('event_api/',views.clientList.as_view()),
    path('event_api/<int:pk>/',views.clientDetail.as_view()),
    path('event_api/project/',views.projectList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
