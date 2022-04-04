from django.urls import path

from . import views

app_name = 'callresp'
 
urlpatterns = [
    path('threads/', views.ThreadListView.as_view(), name='index'),
    path('threads/new', views.new_thread, name='newthread'),
]
