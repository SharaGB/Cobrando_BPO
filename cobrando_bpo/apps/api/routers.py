from rest_framework import routers
from apps.api.viewsets import DepartamentoViewset, EmpleadoViewSet

router = routers.DefaultRouter()

router.register(r'empleados', EmpleadoViewSet, basename='empleados')
router.register(r'departamentos', DepartamentoViewset, basename='departamentos')


urlpatterns = router.urls
