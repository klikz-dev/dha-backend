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
    fields = ['email', 'analysis_name', 'data']
    list_display = ['email', 'analysis_name']
    search_fields = ['email', 'analysis_name']

    inlines = [ReportsInline]


class ReportAdmin(admin.ModelAdmin):
    fields = ['analysis', 'report_name', 'data']
    list_display = ['analysis', 'report_name']
    search_fields = ['analysis', 'report_name']


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(Report, ReportAdmin)
