from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def sec(request):
    return render(request,'sec.html')
