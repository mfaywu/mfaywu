from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'home/index.html')

def contact(request):
	return render(request, 'home/basic.html',{'content':['If you would like to contact me, please email me.','mfaywu@ucla.edu']})
