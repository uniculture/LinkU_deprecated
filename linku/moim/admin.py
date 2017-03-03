from django.contrib import admin
from moim.models import Meeting, User


# Register your models here.

class MeetingAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(User, UserAdmin)
