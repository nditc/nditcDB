from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    path('',include('core.urls')),
    path('apiAuth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
