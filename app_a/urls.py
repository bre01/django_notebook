# app_a urlpatterns

from django.urls import  path


from . import views

app_name='app_a'

urlpatterns=[
    #index
    path('',views.index,name='index'),
    path('sec',views.sec,name='sec'),
    path('topics/',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
]