from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('attendees.urls')),
    path('admin/', admin.site.urls),
]
