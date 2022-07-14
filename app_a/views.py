from django.shortcuts import render,redirect
from .models import Topic
from .forms import TopicForm, EntryForm 
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

#def new_topic(request):
    if request.method != 'POST':
        form=TopicForm()
    else:

        form=TopicForm(data=request.POST)
        if form.iv_valid():
            form.save()
            return redirect('app_a:topics')
    context={'form':form}        
    return render(request,'app_a/new_topic.html',context)
def new_topic(request):
    if request.method=='POST':
        form=TopicForm(data=request.POST)
        if form.iv_valid():
            form.save()
            return redirect('app_a:topics')
    else:
        form=TopicForm()
        context={'form':form}
        return render(request,'app_a/new_topic.html',context)







def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if request.method !='POST':
        form = EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)  
            new_entry.topic=topic 
            new_entry.save()
            return redirect('app_a:topic',topic_id=topic_id)
    context={'topic':topic,'form':form}
    return render(request, 'app_a/new_entry.html',context)