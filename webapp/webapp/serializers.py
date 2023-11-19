from rest_framework.serializers import ModelSerializer
from .models import BankOffer
from rest_framework import serializers


class BankOfferSerializer(ModelSerializer):
    class Meta:
        model = BankOffer
        fields = '__all__'


class QuerySerializer(serializers.Serializer):
    bank_name = serializers.CharField()
    valid_from_date = serializers.DateField()
    dcount = serializers.FloatField()
