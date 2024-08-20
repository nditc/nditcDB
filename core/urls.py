from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.index),
    path('<int:pk>/',views.index),
    path('roll/<int:year>/<str:roll>/',views.roll),
    path('uid/<str:uid>/',views.uniqueID),
    path('year/<int:year>/',views.year),
    path('query/',views.runQuery),
    path('getID/',views.getID),
    path('getToken/',obtain_auth_token),
]