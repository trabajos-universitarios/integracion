from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', tienda, name="tienda"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registrar_usuario/', registrar_usuario, name="registrar_usuario"),
    path('mis_compras/', mis_compras, name="mis_compras"),
    path('detalle_factura/', detalle_factura, name="detalle_factura"),
    path('ficha/<id>', ficha, name="ficha"),
    path('iniciar_pago/<id>', iniciar_pago, name="iniciar_pago"),
    path('pago_exitoso/<id>', pago_exitoso, name="pago_exitoso"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)