from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from app.views import ProductoListView, delete_data

app_name = "app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductoListView.as_view(), name='producto_list'),
    path('reiniciar/', delete_data, name='reiniciar_datos'),

    # path('categorias/add/', CategoryCreateView.as_view(), name='category_create'),
    # path('categorias/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    # path('categorias/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),

    #path('', inicio, name='inicio'),
    # USUARIO
    #path('registrar/', registrar, name='registrar'),
    #path('editar_user/', editar, name='editar_user'),
    #path('editar_passw/', editar_passw, name='editar_passw'),
    #path('entrar/', LoginFormView.as_view(), name='entrar'),
    #path('salir/', LogoutView.as_view(), name='salir'),
    # ESCRITO
    #path('escrito/mostrar/<int:escrito_id>/', ver_escrito, name='escrito'),
    #path('escrito/agregar/', EscritoCreateView.as_view(), name='agregar_escrito'),
    #path('escrito/editar/<int:pk>/', EscritoUpdateView.as_view(), name='editar_escrito'),
    #path('escrito/eliminar/<int:pk>/', EscritoDeleteView.as_view(), name='eliminar_escrito'),
    # COMENTARIO EVALUACION
    #path("escrito/evaluar/<int:escrito_id>/", evaluar_escrito, name="evaluar_escrito"),

    #path('usuario/', usuario, name='usuario'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

