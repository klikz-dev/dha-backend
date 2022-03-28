from rest_framework import serializers

from .models import Analysis, Report, Survey


# Survey
class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class SurveyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['pk']


class SurveyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['email', 'survey_id', 'created_at', 'updated_at']


# Report
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class ReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['pk', 'report_name', 'created_at']


class ReportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['analysis', 'report_name', 'data', 'created_at', 'updated_at']


# Analysis
class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'


class AnalysisListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ['pk', 'analysis_name', 'created_at']


class AnalysisDetailSerializer(serializers.ModelSerializer):
    reports = ReportListSerializer(many=True, read_only=True)

    class Meta:
        model = Analysis
        fields = ['email', 'data', 'analysis_name', 'created_at', 'updated_at', 'reports']
