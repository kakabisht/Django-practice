from django.conf.urls import url
from apptwo import views
from django.urls import path

urlpatterns = [
    path('', views.help, name='help'),

]
