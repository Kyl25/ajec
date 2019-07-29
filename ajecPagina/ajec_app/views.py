from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

# Create your views here.
def base(request):
	return render(request,'base/base.html')