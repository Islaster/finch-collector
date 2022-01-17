# Add the following import
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import *
from .forms import FeedingForm


# Define the home routes
def index(request):
    # Grab all finches/
    finches = Finch.objects.all()
    return render(request,'index.html', {'finches': finches})
# Define the about routes
def about(request):
    return render(request,'about.html')
# Define the details routes
def detail(request, finch_id):
    # Grab one finch
    finch = Finch.objects.get(id=finch_id)
    # Get the toys the finch doesn't have
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=finch.toys.all().values_list('id'))
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form , 'toys': toys_finch_doesnt_have})

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)
#Define create routes
class finchCreate(CreateView):
    model = Finch
    fields = ['name', 'family', 'description']
    success_url = ''
class finchUpdate(UpdateView):
  model = Finch
  fields = ['family', 'description']
    
class finchDelete(DeleteView):
  model = Finch
  success_url = '/'   

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/' 

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('detail', finch_id=finch_id)