from rest_framework import serializers

from .models import Announcement


# Announcement
class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'


class AnnouncementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['title', 'text', 'membership', 'button_text', 'button_link']


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['title', 'text', 'membership', 'button_text', 'button_link', 'created_at', 'created_at']
