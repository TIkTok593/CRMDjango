import random

from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.views import generic
from django.core.mail import send_mail
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin



class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agents_list.html'
    context_object_name = 'agents'  # You can customize your context object name using this variable
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
    
class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agents_create.html'
    form_class = AgentModelForm
    context_object_name = 'agents'  # You can customize your context object name using this variable
    
    def get_queryset(self):
        return Agent.objects.all()

    def get_success_url(self) -> str:
        return reverse('agents:agents-list')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f'{random.randint(0, 1000000)}')
        user.save()
        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )
        send_mail(
            subject='You are invited to be an agent',
            message='You are now an agent in DJCRM website',
            from_email='test@agent.com',
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agents_detail.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        return Agent.objects.all()
    
    
class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agents_update.html'
    form_class = AgentModelForm
    context_object_name = 'agent'
    
    def get_queryset(self):
        return Agent.objects.all()
    
    def get_success_url(self) -> str:
        return reverse('agents:agents-list')
    

class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agents_delete.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        return Agent.objects.all()
    
    def get_success_url(self) -> str:
        return reverse('agents:agents-list')