from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Thread, Response
from .forms import ThreadForm
# Create your views here.

class ThreadListView(generic.ListView):
    template_name = "callresp/index.html"
    context_object_name = "latest_threads_list"
    form = ThreadForm()
    extra_context = {'form':form}
    def get_queryset(self):
        return Thread.objects.order_by('-posted')[:10]

def new_thread(request):
    if request.method == 'POST': 
        form = ThreadForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body  = form.cleaned_data['body']
            t = Thread(title=title, body=body)
            t.save()
            return HttpResponse(str(t))
            
            
