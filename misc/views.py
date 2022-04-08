from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .models import Announcement
from .serializer import AnnouncementDetailSerializer, AnnouncementListSerializer, AnnouncementSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):

    queryset = Announcement.objects.all()
    serializer_class = AnnouncementListSerializer

    def list(self, request):
        announcements = Announcement.objects.all()

        membership = self.request.query_params.get('membership')
        if membership is not None:
            announcements = announcements.filter(membership=membership)

        page = self.paginate_queryset(announcements)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(announcements, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        announcements = Announcement.objects.all()
        announcement = get_object_or_404(announcements, pk=pk)
        serializer = AnnouncementDetailSerializer(
            instance=announcement, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        announcements = Announcement.objects.all()
        announcement = get_object_or_404(announcements, pk=pk)
        serializer = AnnouncementSerializer(data=request.data)

        if serializer.is_valid():
            serializer.update(
                instance=announcement, validated_data=serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        announcements = Announcement.objects.all()
        announcement = get_object_or_404(announcements, pk=pk)
        announcement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
