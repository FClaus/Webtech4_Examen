from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('TimeDifference/', include('TimeDifference.urls')),
    path('admin/', admin.site.urls)
    
]