from rest_framework import serializers
from .models import Cafe, Avaliacao


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = "__all__"


class AvaliacaoSerializer(serializers.ModelSerializer):
    media = serializers.ReadOnlyField()

    class Meta:
        model = Avaliacao
        fields = "__all__"