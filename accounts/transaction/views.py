from rest_framework import generics
from rest_framework.mixins import CreateModelMixin
from rest_framework import status
from rest_framework.response import Response

from .serializers import AccountSerializer
from .models import Accounts

class AccountsList(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Accounts.objects.all()

class AccountsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AccountSerializer
    queryset = Accounts.objects.filter()    