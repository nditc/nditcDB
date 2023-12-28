from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.index),
    path('<int:pk>/',views.index),
    path('year/<int:year>/',views.year),
    path('query/',views.runQuery),
    path('getID/',views.getID),
    path('getToken/',obtain_auth_token),
]