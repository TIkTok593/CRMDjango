from django import forms
from django.contrib.auth import get_user_model


user = get_user_model()    


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = user
        fields = (
            'email',
            'username',
            'first_name',
            'last_name'
        )