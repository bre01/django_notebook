from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Topic,Entry
from .forms import TopicForm, EntryForm


# Create your views here.
def index(request):
    return render(request, 'app_a/index.html')


def sec(request):
    return render(request, 'app_a/sec.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics, 'test': [1,2,3,4]}
    return render(request, 'app_a/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'app_a/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:

        form = TopicForm(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect('app_a:topics')
    context = {'form': form}
    return render(request, 'app_a/new_topic.html', context)


#def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_a:topics')
    else:
        form = TopicForm()
        context = {'form': form}
        return render(request, 'app_a/new_topic.html', context)


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('app_a:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'app_a/new_entry.html', context)

def edit_entry(request,entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic
    if request.mothod !='POST':
        form=EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_a/topic',topic_id=topic.id)
    context={'entry':entry,'topic':topic,'form':form}
    return render(request,'app_a/edit_entry.html',context)
