from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OrganizerAndLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not self.request.user.is_organizer:
            return redirect('leads:lead-list')
        return super().dispatch(request, *args, **kwargs)
