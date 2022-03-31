from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from qualtrics.models import Analysis, Report, Survey
from qualtrics.serializer import AnalysisDetailSerializer, AnalysisListSerializer, AnalysisSerializer, ReportDetailSerializer, ReportListSerializer, ReportSerializer, SurveyDetailSerializer, SurveyListSerializer, SurveySerializer


class SurveyViewSet(viewsets.ModelViewSet):

    queryset = Survey.objects.all()
    serializer_class = SurveyListSerializer

    def list(self, request):
        surveys = Survey.objects.all()

        email = self.request.query_params.get('email')
        if email is not None:
            surveys = surveys.filter(email=email)

        page = self.paginate_queryset(surveys)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(surveys, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        surveys = Survey.objects.all()
        survey = get_object_or_404(surveys, pk=pk)
        serializer = SurveyDetailSerializer(
            instance=survey, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = SurveySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        surveys = Survey.objects.all()
        survey = get_object_or_404(surveys, pk=pk)
        serializer = SurveySerializer(data=request.data)

        if serializer.is_valid():
            serializer.update(
                instance=survey, validated_data=serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        surveys = Survey.objects.all()
        survey = get_object_or_404(surveys, pk=pk)
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AnalysisViewSet(viewsets.ModelViewSet):

    queryset = Analysis.objects.all()
    serializer_class = AnalysisListSerializer

    def list(self, request):
        analytics = Analysis.objects.all()

        email = self.request.query_params.get('email')
        if email is not None:
            analytics = analytics.filter(email=email)

        page = self.paginate_queryset(analytics)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(analytics, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        analytics = Analysis.objects.all()
        analysis = get_object_or_404(analytics, pk=pk)
        serializer = AnalysisDetailSerializer(
            instance=analysis, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = AnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        analytics = Analysis.objects.all()
        analysis = get_object_or_404(analytics, pk=pk)
        serializer = AnalysisSerializer(data=request.data)

        if serializer.is_valid():
            serializer.update(
                instance=analysis, validated_data=serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        analytics = Analysis.objects.all()
        analysis = get_object_or_404(analytics, pk=pk)
        analysis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReportViewSet(viewsets.ModelViewSet):

    queryset = Report.objects.all()
    serializer_class = ReportListSerializer

    def list(self, request):
        reports = Report.objects.all()

        email = self.request.query_params.get('email')
        if email is not None:
            reports = reports.filter(analysis__email=email)

        analysis = self.request.query_params.get('analysis')
        if analysis is not None:
            reports = reports.filter(analysis=analysis)

        page = self.paginate_queryset(reports)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(reports, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        reports = Report.objects.all()
        report = get_object_or_404(reports, pk=pk)
        serializer = ReportDetailSerializer(
            instance=report, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        reports = Report.objects.all()
        report = get_object_or_404(reports, pk=pk)
        serializer = ReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.update(
                instance=report, validated_data=serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        reports = Report.objects.all()
        report = get_object_or_404(reports, pk=pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
