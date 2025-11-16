from django.urls import path
from . import views

urlpatterns = [
    # Página de inicio
    path('', views.HomeView.as_view(), name='home'),

    # Productos
    path('productos/', views.ProductoListView.as_view(), name='lista_productos'),
    path('productos/crear/', views.ProductoCreateView.as_view(), name='crear_producto'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='detalle_producto'),
    path('productos/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='editar_producto'),
    path('productos/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='eliminar_producto'),

    # Categorías
    path('categorias/', views.CategoriaListView.as_view(), name='lista_categorias'),
    path('categorias/crear/', views.CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='eliminar_categoria'),
    path('categorias/<int:pk>/filtro', views.filtro_categorias, name='filtro_categorias'),

    # Etiquetas
    path('etiquetas/', views.EtiquetaListView.as_view(), name='lista_etiquetas'),
    path('etiquetas/crear/', views.EtiquetaCreateView.as_view(), name='crear_etiqueta'),
    path('etiquetas/<int:pk>/editar/', views.EtiquetaUpdateView.as_view(), name='editar_etiqueta'),
    path('etiquetas/<int:pk>/eliminar/', views.EtiquetaDeleteView.as_view(), name='eliminar_etiqueta'),
    path('etiquetas/<int:pk>/filtro', views.filtro_etiquetas, name='filtro_etiquetas'),
]