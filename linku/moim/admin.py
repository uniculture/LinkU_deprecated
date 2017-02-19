from django.contrib import admin
from moim.models import Meeting


# Register your models here.

class MeetingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Meeting, MeetingAdmin)
