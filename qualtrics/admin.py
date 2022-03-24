from django.contrib import admin
from qualtrics.models import Analysis, Report, Survey


class SurveyAdmin(admin.ModelAdmin):
    fields = ['email', 'survey_id']
    list_display = ['email', 'survey_id']
    search_fields = ['email', 'survey_id']


class ReportsInline(admin.TabularInline):
    model = Report
    extra = 0


class AnalysisAdmin(admin.ModelAdmin):
    fields = ['email', 'data']
    list_display = ['email']
    search_fields = ['email']

    inlines = [ReportsInline]


class ReportAdmin(admin.ModelAdmin):
    fields = ['analysis', 'data']
    list_display = ['analysis']
    search_fields = ['analysis']


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(Report, ReportAdmin)
