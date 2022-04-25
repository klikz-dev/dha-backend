from django.contrib import admin

from misc.models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'membership', 'button_text', 'button_link']

    list_filter = ['membership', ]
    list_display = ['title', 'membership', 'button_text', 'button_link']
    search_fields = ['title', 'text', 'button_text', 'button_link']


admin.site.register(Announcement, AnnouncementAdmin)
