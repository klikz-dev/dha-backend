from rest_framework import serializers

from .models import Membership


# Membership
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'


class MembershipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['email', 'membership', 'acute',
                  'ambulatory', 'ltpac', 'organization_name', 'created_at', 'updated_at']


class MembershipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['email', 'membership', 'acute',
                  'ambulatory', 'ltpac', 'organization_name', 'created_at', 'updated_at']
