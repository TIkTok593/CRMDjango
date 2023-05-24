from django.contrib import admin
from leads.models import Lead, Agent, User, UserProfile


admin.site.register([User, Lead, Agent, UserProfile])