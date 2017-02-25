from django.http import HttpResponse
from moim.models import Meeting
from django.shortcuts import render


def homepage(request):
    meetings = Meeting.objects.all()
    return render(request, 'meeting_list.html', {'meetings': meetings})


def apply_meeting(request, meeting_id):
    meeting = Meeting.objects.get(id=meeting_id)
    return render(request, 'apply_meeting.html', {'meeting': meeting})
