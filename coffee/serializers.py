from rest_framework import serializers
from .models import Cafe, Avaliacao


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = "__all__"


class AvaliacaoSerializer(serializers.ModelSerializer):
    media = serializers.SerializerMethodField()

    class Meta:
        model = Avaliacao
        fields = "__all__"

    def get_media(self, obj):
        return round(obj.media_avaliacao, 1)