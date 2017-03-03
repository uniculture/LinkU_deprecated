from moim.models import Meeting, Applier, User
from django.shortcuts import render, redirect


def sign_up(request):
    if request.method == 'POST':
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        phone3 = request.POST['phone3']

        User.objects.create(email=request.POST['email'], password=request.POST['password'],
                            gender=request.POST['gender'],
                            nickname=request.POST['nickname'], phone_number=phone1 + phone2 + phone3)

        return redirect('/')

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
