from django.http import HttpResponse
from moim.models import Meeting


def homepage(request):
    content = ''
    for obj in Meeting.objects.all():
        content += obj.name + "\n"
    return HttpResponse(content)
