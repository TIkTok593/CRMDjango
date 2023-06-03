from django.contrib import admin
from leads.models import Lead, Agent, User, UserProfile, Category


class LeadAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'second_name',
        'age',
        'email',
    )
    list_display_links = ('first_name',)  # the list of fields that can be <a> html tag
    list_editable = ('second_name',)  # this field can be edited from the menu also, before navigating to the object's configuration page.
    search_fields = ('first_name', 'second_name', 'age')
    list_filter = ('category', )
    

admin.site.register(User)
admin.site.register(Lead, LeadAdmin)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)