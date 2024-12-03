from __future__ import absolute_import
from django.urls import path, re_path

from . import views


app_name = 'oauth2_provider'


base_urlpatterns = [
    path('authorize/', views.AuthorizationView.as_view(), name="authorize"),
    path('token/', views.TokenView.as_view(), name="token"),
    path('revoke_token/', views.RevokeTokenView.as_view(), name="revoke-token"),
]


management_urlpatterns = [
    # Application management views
    path('applications/', views.ApplicationList.as_view(), name="list"),
    path('applications/register/', views.ApplicationRegistration.as_view(), name="register"),
    re_path(r'^applications/(?P<pk>[\w-]+)/$', views.ApplicationDetail.as_view(), name="detail"),
    re_path(r'^applications/(?P<pk>[\w-]+)/delete/$', views.ApplicationDelete.as_view(), name="delete"),
    re_path(r'^applications/(?P<pk>[\w-]+)/update/$', views.ApplicationUpdate.as_view(), name="update"),
    # Token management views
    path('authorized_tokens/', views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
    re_path(r'^authorized_tokens/(?P<pk>[\w-]+)/delete/$', views.AuthorizedTokenDeleteView.as_view(),
        name="authorized-token-delete"),
]


urlpatterns = base_urlpatterns + management_urlpatterns
