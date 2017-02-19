from django.http import HttpResponse
from moim.models import Meeting
from django.shortcuts import render


def homepage(request):
    meetings = Meeting.objects.all()
    return render(request, 'meeting_list.html', {'meetings': meetings})
