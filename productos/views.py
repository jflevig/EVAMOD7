from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Producto, Categoria, Etiqueta, Detalle
from .forms import ProductoForm, CategoriaForm, EtiquetaForm, DetalleForm
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'index.html'

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos_lista.html'
    context_object_name = 'productos'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos_crear.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['detalle_form'] = DetalleForm(self.request.POST)
        else:
            context['detalle_form'] = DetalleForm()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detalle_form = context['detalle_form']
        if detalle_form.is_valid():
            self.object = form.save()
            detalle = detalle_form.save(commit=False)
            detalle.producto = self.object
            detalle.save()
            return redirect(reverse_lazy('lista_productos'))
        else:
            return self.form_invalid(form)


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos_detalle.html'
    context_object_name = 'producto'

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos_editar.html'
    success_url = reverse_lazy('lista_productos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.object

        try: 
            detalle = producto.detalle
        except Detalle.DoesNotExist:
            detalle = Detalle(producto=producto)

        if self.request.POST:
            context['detalle_form'] = DetalleForm(self.request.POST, instance=detalle)
        else:
            context['detalle_form'] = DetalleForm(instance=detalle)
        
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        detalle_form = context['detalle_form']

        if detalle_form.is_valid():
            self.object = form.save()
            detalle = detalle_form.save(commit=False)
            detalle.producto = self.object
            detalle.save()
            return redirect(reverse_lazy('lista_productos'))
        else:
            return self.form_invalid(form)

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos_eliminar.html'
    success_url = reverse_lazy('lista_productos')

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias_lista.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias_crear.html'
    success_url = reverse_lazy('lista_categorias')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias_editar.html'
    success_url = reverse_lazy('lista_categorias')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categorias_eliminar.html'
    success_url = reverse_lazy('lista_categorias')

def filtro_categorias(request, pk):
    categoria = Categoria.objects.get(id=pk)
    productos_filtrados = categoria.productos.all()
    return render(request, 'productos_lista.html', {'productos': productos_filtrados})

class EtiquetaListView(ListView):
    model = Etiqueta
    template_name = 'etiquetas_lista.html'
    context_object_name = 'etiquetas'

class EtiquetaCreateView(CreateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = 'etiquetas_crear.html'
    success_url = reverse_lazy('lista_etiquetas')

class EtiquetaUpdateView(UpdateView):
    model = Etiqueta
    form_class = EtiquetaForm
    template_name = 'etiquetas_editar.html'
    success_url = reverse_lazy('lista_etiquetas')

class EtiquetaDeleteView(DeleteView):
    model = Etiqueta
    template_name = 'etiquetas_eliminar.html'
    success_url = reverse_lazy('lista_etiquetas')

def filtro_etiquetas(request, pk):
    etiqueta = Etiqueta.objects.get(id=pk)
    productos_filtrados = etiqueta.productos.all()
    return render(request, 'productos_lista.html', {'productos': productos_filtrados})