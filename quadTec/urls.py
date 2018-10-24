from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travel.urls')),
    ]