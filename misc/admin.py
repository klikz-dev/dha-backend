from django.contrib import admin

from misc.models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'membership']

    list_filter = ['membership', ]
    list_display = ['title', 'membership']
    search_fields = ['title', 'text']


admin.site.register(Announcement, AnnouncementAdmin)
