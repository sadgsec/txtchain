from django.urls import path

from . import views

app_name = 'callresp'
 
urlpatterns = [
    path('', views.ThreadListView.as_view(), name='index'),
    path('new', views.new_thread, name='newthread'),
]
