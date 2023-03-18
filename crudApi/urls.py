from rest_framework import routers
from .api import UsuarioViewSet,SolicitudViewSet,RecordatorioViewSet,ReporteViewSet
from . import views

router = routers.DefaultRouter()

router.register('api/usuarios',UsuarioViewSet,'usuarios')
router.register('api/solicitudes',SolicitudViewSet,'solicitudes')
router.register('api/recordatorios',RecordatorioViewSet,'recordatorios')
router.register('api/reportes',ReporteViewSet,'reportes')





urlpatterns = router.urls

