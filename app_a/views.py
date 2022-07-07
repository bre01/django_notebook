from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm 
# Create your views here.
def index(request):
    return render(request,'app_a/index.html')

def sec(request):
    return render(request,'app_a/sec.html')

def topics(request):
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics,'test':[]}
    return render(request,'app_a/topics.html',context)

def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    context={'topics':topics,'entries':entries}
    return render(request,'app_a/topic.html',context)

def new_topic(request):
    if request.method != 'POST':
        form=TopicForm()
    else:

        form=TopicForm(data=request.POST)
        if form.iv_valid():
            form.save()
            return redirect('app_a:topics')
    context={'form':form}        
    return render(request,'app_a/new_topic.html',context)