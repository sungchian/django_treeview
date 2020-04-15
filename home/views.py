from django.shortcuts import render, HttpResponse
from .models import Member
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def listone(request):
    try:
        unit = Member.objects.get(name = 'Taiwan')
    except:
        errormessage = "讀取錯誤！！"
    return render(request, 'home/listone.html', locals())

def listall(request):
    states = Member.objects.all().order_by('level')
    return render(request, 'home/listall.html', locals())