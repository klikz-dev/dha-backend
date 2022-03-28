from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from membersuite.models import Membership
from membersuite.serializer import MembershipDetailSerializer, MembershipListSerializer, MembershipSerializer


class MembershipViewSet(viewsets.ModelViewSet):

    queryset = Membership.objects.all()
    serializer_class = MembershipListSerializer

    def list(self, request):
        memberships = Membership.objects.all()

        email = self.request.query_params.get('email')
        if email is not None:
            memberships = memberships.filter(email=email)

        page = self.paginate_queryset(memberships)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(memberships, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        memberships = Membership.objects.all()
        membership = get_object_or_404(memberships, pk=pk)
        serializer = MembershipDetailSerializer(
            instance=membership, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        memberships = Membership.objects.all()
        membership = get_object_or_404(memberships, pk=pk)
        serializer = MembershipSerializer(data=request.data)

        if serializer.is_valid():
            serializer.update(
                instance=membership, validated_data=serializer.validated_data)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        memberships = Membership.objects.all()
        membership = get_object_or_404(memberships, pk=pk)
        membership.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
