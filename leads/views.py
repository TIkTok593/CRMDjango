from typing import Any, Dict
from django.core.mail import send_mail
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm
from .mixins import OragnizerAndLoginRequiredMixin


class LandingPageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'landing.html'
    

class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'  # You can customize your context object name using this variable
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        if user.is_organizer:
            leads = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)  # if the user is only organizer it'll have a userprofile
        else:
            leads = Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
            leads = leads.filter(agent__user=user)
        return leads  # by default this will be passed to the template with object_list => because it's a list view
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
            context.update({
                'unassigned_leads': queryset
            })
        return context


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    context_object_name = 'lead'
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        if user.is_organizer:
            leads = Lead.objects.filter(organization=user.userprofile)  # if the user is only organizer it'll have a userprofile
        else:
            leads = Lead.objects.filter(organization=user.agent.organization)
            leads = leads.filter(agent__user=user)
        return leads  # by default this will be passed to the template with object_list => because it's a list view



class LeadCreateView(OragnizerAndLoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead_create.html'
    queryset = Lead.objects.all()
    form_class = LeadForm

    
    def get_success_url(self) -> str:
        return reverse('leads:lead-list')
    
    def form_valid(self, form):
        send_mail(
            subject='Assalam Alikum',
            message='كيف حالك',
            from_email='abuyahyadiab@gmail.com',
            recipient_list=[
                'abdlearning593@gmail.com'
            ]
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadForm
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)  # by default this will be passed to the template with object_list => because it's a list view

    
    def get_success_url(self) -> str:
        return reverse('leads:lead-list')
    

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        return Lead.objects.filter(organization=user.userprofile)  # by default this will be passed to the template with object_list => because it's a list view
    
    def get_success_url():
        return reverse('leads:lead-list')
