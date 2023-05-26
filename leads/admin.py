from django.contrib import admin
from leads.models import Lead, Agent, User, UserProfile, Category


admin.site.register([User, Lead, Agent, UserProfile, Category])