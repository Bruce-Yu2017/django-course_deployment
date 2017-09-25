# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

def index(request):
  context = {'courses': Course.objects.all()}
  return render(request, 'add_course/index.html', context)

def add_new(request):
  if request.method == "POST":
    print request.POST
    errors = Course.objects.create_validator(request.POST)
    if len(errors):
      for tag, error in errors.iteritems():
        messages.error(request, error, extra_tags = tag)
      return redirect('/')
    else:
      Course.objects.create(name = request.POST['name'], description = request.POST['description'])
      return redirect('/')

def confirm_remove(request, id):
  context = {'courses': Course.objects.get(id=id)}
  return render(request, 'add_course/remove.html', context)

def remove(request, id):
  context = {'courses': Course.objects.get(id=id)}
  re = Course.objects.get(id=id)
  if re:
    re.delete()
  return redirect('/')














