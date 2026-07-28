from django.contrib import admin
from .models import Cafe, Avaliacao

# Register your models here.



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