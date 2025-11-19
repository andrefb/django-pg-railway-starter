from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'clientes/list.html'
    context_object_name = 'clientes'

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
