from django.conf.urls import url
from . import views
from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'travel'
urlpatterns = [

    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    path('trip/new/', views.trip_request_new, name='trip_request_new'),
    path('trip/<int:pk>/dept_city/', views.trip_req_dept_city, name='trip_req_dept_city'),

    ]


