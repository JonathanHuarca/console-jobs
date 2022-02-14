
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView

from .models import Company, Identifier, Postulant, Postulation, WorkOffer
from .serializers import (CompanySerializer, IdentifierSerializer,
                          PostulantSerializer, PostulationSerializer,
                          WorkOfferSerializer)


class PostulantListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Postulant.objects.filter(is_active=True)
    serializer_class = PostulantSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter
    )
    filterset_fields = {
        "user": ['exact'],
        "user__username": ['exact'],
        "user__email": ['exact'],
        "user__first_name": ['exact'],
        "user__last_name": ['exact'],
        "identifier_number": ['exact']
    }
    search_fields = [
        '$user__username',
        '$user__email',
        '$user__first_name',
        '$user__last_name',
        '$identifier_number',
    ]


class PostulantDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Postulant.objects.filter(is_active=True)
    serializer_class = PostulantSerializer


class CompanyListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter
    )
    filterset_fields = {
        "bussines_name": ['exact'],
        "user": ['exact'],
        "user__username": ['exact'],
        "user__email": ['exact'],
        "user__first_name": ['exact'],
        "user__last_name": ['exact'],
        "identifier_number": ['exact']
    }
    search_fields = [
        '$user__username',
        '$user__email',
        '$user__first_name',
        '$user__last_name',
        '$identifier_number',
        '$description',
    ]


class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Company.objects.filter(is_active=True)
    serializer_class = CompanySerializer


class IdentifierListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Identifier.objects.filter(is_active=True)
    serializer_class = IdentifierSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter
    )
    filterset_fields = {
        "name": ['exact'],
        "code": ['exact'],
    }
    search_fields = [
        '$name',
        '$code',
    ]


class IdentifierDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Identifier.objects.filter(is_active=True)
    serializer_class = IdentifierSerializer


class WorkOfferListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = WorkOffer.objects.filter(is_active=True)
    serializer_class = WorkOfferSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter
    )
    filterset_fields = {
        "company": ['exact'],
        "company__bussines_name": ['exact'],
        "title": ['exact'],
        "target_rol": ['exact'],
        "salary": ['exact', 'lt', 'lte', 'gte', 'gt'],
        "job_type": ['exact'],
    }
    search_fields = [
        '$company__bussines_name',
        '$title',
        '$description',
    ]


class WorkOfferDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = WorkOffer.objects.filter(is_active=True)
    serializer_class = WorkOfferSerializer


class PostulationListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Postulation.objects.filter(is_active=True)
    serializer_class = PostulationSerializer
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter
    )
    filterset_fields = {
        "work_offer": ['exact'],
        "work_offer__title": ['exact'],
        "work_offer__company": ['exact'],
        "work_offer__company__user": ['exact'],
        "work_offer__company__bussines_name": ['exact'],
        "postulant": ['exact'],
        "postulant__user": ['exact'],
        "postulant__user__username": ['exact'],
        "postulant__user__email": ['exact'],
    }
    search_fields = [
        '$work_offer__title',
        '$work_offer__company__bussines_name',
        '$postulant__user__username',
        '$postulant__user__email',
    ]


class PostulationDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Postulation.objects.filter(is_active=True)
    serializer_class = PostulationSerializer
