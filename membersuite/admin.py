from django.contrib import admin
from membersuite.models import Membership


class MembershipAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['email', 'membership']}),
        ('DHMW Reports', {'fields': ['acute', 'ambulatory', 'ltpac']}),
    ]

    list_filter = ['membership']
    list_display = ['email', 'membership', 'acute', 'ambulatory', 'ltpac']
    search_fields = ['email', 'membership', 'acute', 'ambulatory', 'ltpac']


admin.site.register(Membership, MembershipAdmin)
