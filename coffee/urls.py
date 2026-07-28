from rest_framework.routers import DefaultRouter

from .views import CafeViewSet, AvaliacaoViewSet

router = DefaultRouter()

router.register(r"cafes", CafeViewSet, basename="cafes")
router.register(r"avaliacoes", AvaliacaoViewSet, basename="avaliacoes")

urlpatterns = router.urls