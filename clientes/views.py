from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.db.models import Q, Func
from django.core.paginator import Paginator
from .models import Cliente

class OnlyDigits(Func):
    function = 'REGEXP_REPLACE'
    template = "%(function)s(%(expressions)s, '[^0-9]', '', 'g')"

def clientes_list(request):
    query = request.GET.get('q', '').strip()
    clientes = Cliente.objects.all()
    if query:
        search_digits = ''.join(filter(str.isdigit, query))
        # Se o termo tem algum número, faz filtro especial, senão, só busca textual
        if search_digits:
            clientes = clientes.annotate(
                telefone_digits=OnlyDigits('telefone'),
                cpf_digits=OnlyDigits('cpf')
            ).filter(
                Q(nome__icontains=query) |
                Q(email__icontains=query) |
                Q(telefone__icontains=query) |
                Q(cpf__icontains=query) |
                Q(telefone_digits__icontains=search_digits) |
                Q(cpf_digits__icontains=search_digits)
            )
        else:
            clientes = clientes.filter(
                Q(nome__icontains=query) |
                Q(email__icontains=query) |
                Q(telefone__icontains=query) |
                Q(cpf__icontains=query)
            )
    clientes = clientes.order_by('nome')
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'clientes/list.html', {
        'clientes': page_obj,
        'page_title': 'Clientes'
    })




class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'clientes/view.html'
    context_object_name = 'cliente'

class ClienteEditView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'clientes/edit.html'
    form_class = ClienteForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.id_usuario_update = self.request.user
        obj.save()
        return redirect('clientes:view', pk=obj.pk)
