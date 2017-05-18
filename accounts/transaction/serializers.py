from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import Accounts

class AccountSerializer(ModelSerializer):

    class Meta:
        model = Accounts
        fields = (
            'id',
            'label',
        )
        read_only_fields = (
            'id',
        )
