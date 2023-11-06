from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = { 'mymembers': mymembers }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymembers = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = { 'mymembers': mymembers }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('testing.html')
    context = { 
        'fruits' : ['Apple', "Banana", "Cherry", "Dragon Fruit", "Elephant Apple"],
        'x': ['Apple', 'Banana', 'Cherry'],
        'y': ['Apple', 'Banana', 'Cherry'],
        }
    return HttpResponse(template.render(context, request))