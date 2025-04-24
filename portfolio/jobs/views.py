from django.shortcuts import render
from .models import Job #MODEL CLASS


# Create your views here.
def homepage(request):
    jobs=Job.objects.all()
    return render(request,'jobs/home.html',{'jobs':jobs})