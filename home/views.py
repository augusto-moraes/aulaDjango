# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
    numbers = [1, 2, 3, 4, 5]
    myName = 'Augusto'

    args = {'name' : myName}
    return render(request, 'home/index.html', args)

def aula(request):
    return render(request, 'home/aula.html')
