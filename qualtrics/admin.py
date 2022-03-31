from django.contrib import admin
from qualtrics.models import Analysis, Report, Survey
from django.db import models
from django_json_widget.widgets import JSONEditorWidget


class SurveyAdmin(admin.ModelAdmin):
    fields = ['email', 'survey_id', 'data']
    list_display = ['email', 'survey_id']
    search_fields = ['email', 'survey_id']

    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


class ReportsInline(admin.TabularInline):
    model = Report
    extra = 0


class AnalysisAdmin(admin.ModelAdmin):
    fields = ['email', 'analysis_name', 'data']
    list_display = ['email', 'analysis_name']
    search_fields = ['email', 'analysis_name']

    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

    inlines = [ReportsInline]


class ReportAdmin(admin.ModelAdmin):
    fields = ['analysis', 'report_name', 'data']
    list_display = ['analysis', 'report_name']
    search_fields = ['analysis', 'report_name']

    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(Report, ReportAdmin)
