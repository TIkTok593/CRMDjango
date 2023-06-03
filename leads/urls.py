from django.urls import path
from .views import (
        LeadListView, 
        LeadDetailView, 
        LeadUpdateView, 
        LeadCreateView, 
        LeadDeleteView, 
        AssginAgentView, 
        CategoryListView,
        CategoryDetailView,
        LeadCategoryUpdateView,
        LeadJsonView,
        FollowupCreateView,
        FollowupUpdateView
    )

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('json/', LeadJsonView.as_view(), name='lead-list-json'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('<int:pk>/assign-agent/', AssginAgentView.as_view(), name='assign-agent'),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name='lead-category-update'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('<int:pk>/followup/create/', FollowupCreateView.as_view(), name='followup-create'),
    path('followup/<int:pk>/', FollowupUpdateView.as_view(), name='followup-update'),
]
