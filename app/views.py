from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from app.models import Producto


class ProductoListView(ListView):
    model = Producto
    template_name = 'view_producto.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # PASA LOS DATOS A LA VISTA
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['create_url'] = reverse_lazy('erp:category_create')
        # context['list_url'] = reverse_lazy('erp:category_list')
        productos = Producto.objects.filter(active=True).order_by('orden')
        importe_total = 0
        for p in productos:
            importe_total = importe_total + p.importe
        context['productos'] = productos
        context['importe_total'] = importe_total
        return context


def delete_data(request):
    if request.method == 'POST':
    #   ELIMINAR AQUI
        Producto.objects.all().update(inicio=0, entrada=0, final=0, venta=0, importe=0.00)
        return HttpResponseRedirect(reverse_lazy("app:producto_list"))
        # reverse_lazy("view_producto.html")
        # return render(request, "view_producto.html")


###############GUIARME POR ESTO Y POR EL DE ABAJO


# class EscritoCreateView(CreateView):
#     model = Escrito
#     form_class = EscritoForm
#     template_name = 'erp/agregar_escrito.html'
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'add':
#                 form = self.get_form()
#                 data = form.save()
#                 return redirect('erp:usuario')
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     # PASA LOS DATOS A LA VISTA
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         autor = self.request.user.id
#         user = User.objects.get(id=autor)
#         categorias = Categoria.objects.filter(active=True)
#         context['user'] = user
#         context['categorias'] = categorias
#         context['action'] = 'add'
#         return context
#
#
# class EscritoUpdateView(UpdateView):
#     model = Escrito
#     form_class = EscritoForm
#     template_name = 'erp/agregar_escrito.html'
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'edit':
#                 form = self.get_form()
#                 data = form.save()
#                 return redirect('erp:usuario')
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     # PASA LOS DATOS A LA VISTA
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         autor = self.request.user.id
#         user = User.objects.get(id=autor)
#         categorias = Categoria.objects.filter(active=True)
#         context['user'] = user
#         context['categorias'] = categorias
#         context['action'] = 'edit'
#         context['pk'] = self.kwargs.get('pk')
#         return context
#
#
# class EscritoDeleteView(DeleteView):
#     model = Escrito
#     template_name = reverse_lazy('erp:usuario')
#     success_url = reverse_lazy('erp:usuario')
#     url_redirect = success_url
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             self.object.delete()
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['list_url'] = self.success_url
#         return context
#
#
# ###############GUIARME POR ESTO
#
# class CategoryListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
#     permission_required = 'erp.view_category'
#     model = Category
#     template_name = 'categorias/list.html'
#
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     # sobreescribir metodo post
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'searchdata':
#                 data = []
#                 for i in Category.objects.all():
#                     data.append(i.toJSON())
#             else:
#                 data['error'] = 'Ha ocurrido un error'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)
#
#     # PASA LOS DATOS A LA VISTA
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Listado de Categorias"
#         context['create_url'] = reverse_lazy('erp:category_create')
#         context['list_url'] = reverse_lazy('erp:category_list')
#         context['entity'] = 'Categorias'
#         return context
#
#
# class CategoryCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'categorias/create.html'
#     permission_required = 'erp.add_category'
#     success_url = reverse_lazy('erp:category_list')
#     url_redirect = success_url
#
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'add':
#                 form = self.get_form()
#                 data = form.save()
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     # PASA LOS DATOS A LA VISTA
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Creacion de una categoria"
#         context['entity'] = 'Categorias'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         return context
#
#
# class CategoryUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
#     permission_required = 'erp.change_category'
#     model = Category
#     form_class = CategoryForm
#     template_name = 'categorias/create.html'
#     success_url = reverse_lazy('erp:category_list')
#     url_redirect = success_url
#
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'edit':
#                 form = self.get_form()
#                 data = form.save()
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opcion'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Edicion de una categoria"
#         context['entity'] = 'Categorias'
#         context['list_url'] = self.success_url
#         context['action'] = 'edit'
#         return context
#
#
# class CategoryDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
#     permission_required = 'erp.delete_category'
#     model = Category
#     template_name = 'categorias/delete.html'
#     success_url = reverse_lazy('erp:category_list')
#     url_redirect = success_url
#
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             self.object.delete()
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = "Eliminacion de una categoria"
#         context['entity'] = 'Categorias'
#         context['list_url'] = self.success_url
#         return context