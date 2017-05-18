from django.conf.urls import url
from transaction import views

urlpatterns = [
#    url(r'^(?P<pk>\d+)/$', views.AccountsDetails.as_view(), name="accounts-details"),
#    url(r'^$', views.AccountsList.as_view(), name="accounts-list"),
     url(r'^accounts/$', views.AccountsList.as_view(), name="transaction.accounts.list"),
     url(r'^accounts/(?P<pk>\d+)/$', views.AccountsDetails.as_view(), name="transaction.accounts.details"),
]