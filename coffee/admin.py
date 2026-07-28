from django.contrib import admin
from .models import Cafe, Avaliacao


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "produtor")
    search_fields = ("nome", "produtor")


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cafe",
        "media",
        "criado_em",
    )
    list_filter = ("criado_em",)
    search_fields = ("cafe__nome",)

    @admin.display(description="Média")
    def media(self, obj):
        return round(obj.media_avaliacao, 1)