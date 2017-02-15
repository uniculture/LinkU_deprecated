from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('돈까스 모임')
