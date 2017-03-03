from moim.models import Meeting, Applier
from django.shortcuts import render, redirect


def sign_up(request):
    return render(request, 'sign_up.html')

def homepage(request):
    meetings = Meeting.objects.all()
    return render(request, 'meeting_list.html', {'meetings': meetings})


def apply_meeting(request, meeting_id):
    meeting = Meeting.objects.get(id=meeting_id)
    if request.method == 'GET':
        return render(request, 'apply_meeting.html', {'meeting': meeting})

    elif request.method == 'POST':
        Applier.objects.create(name=request.POST['name'], phone_number=request.POST['phone_number'],
                               gender=request.POST['gender'], meeting=meeting)
        return redirect('/')
