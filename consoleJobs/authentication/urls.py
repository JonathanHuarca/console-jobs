from django.urls import path, re_path

from .views import LoginAPIView, SignUpAPIView, UserListView

urlpatterns = [
    re_path(r'^login/', LoginAPIView.as_view(), name='user-login'),
    path('signup/', SignUpAPIView.as_view(), name='user-login'),
    path('users/', UserListView.as_view(), name='users'),
]
