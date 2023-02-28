from rest_framework import routers
from .api import UsuarioViewSet,SolicitudViewSet

router = routers.DefaultRouter()

router.register('api/usuarios',UsuarioViewSet,'usuarios')
router.register('api/solicitudes',SolicitudViewSet,'solicitudes')

urlpatterns = router.urls
