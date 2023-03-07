from rest_framework import routers
from .api import UsuarioViewSet,SolicitudViewSet,RecordatorioViewSet
from . import views

router = routers.DefaultRouter()

router.register('api/usuarios',UsuarioViewSet,'usuarios')
router.register('api/solicitudes',SolicitudViewSet,'solicitudes')
router.register('api/recordatorios',RecordatorioViewSet,'recordatorios')


urlpatterns = router.urls

