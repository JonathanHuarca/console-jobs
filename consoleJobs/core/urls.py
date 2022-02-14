from django.urls import path

from core.views import (CompanyDetailView, CompanyListView,
                        IdentifierDetailView, IdentifierListView,
                        PostulantDetailView, PostulantListView, PostulationDetailView, PostulationListView,
                        WorkOfferDetailView, WorkOfferListView)

urlpatterns = [
    # Postulants
    path("postulants/", PostulantListView.as_view(), name="postulants"),
    path("postulants/<int:pk>/", PostulantDetailView.as_view(),
         name="postulants-detail"),

    # Companies
    path("companies/", CompanyListView.as_view(), name="companies"),
    path("companies/<int:pk>/", CompanyDetailView.as_view(),
         name="companies-detail"),

    # Identifiers
    path("identifiers/", IdentifierListView.as_view(), name="identifiers"),
    path("identifiers/<int:pk>/", IdentifierDetailView.as_view(),
         name="identifiers-detail"),

    # Work Offers
    path("work-offers/", WorkOfferListView.as_view(), name="work-offers"),
    path("work-offers/<int:pk>/", WorkOfferDetailView.as_view(),
         name="work-offers-detail"),

    # Postulations
    path("postulations/", PostulationListView.as_view(), name="postulations"),
    path("postulations/<int:pk>/", PostulationDetailView.as_view(),
         name="postulations-detail"),
]
