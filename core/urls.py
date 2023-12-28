from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:pk>/',views.index),
    path('year/<int:year>/',views.year),
    path('query/',views.runQuery),
    path('getID/',views.getID)
]