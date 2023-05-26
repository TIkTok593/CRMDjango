from django import forms
from .models import Lead, Agent, User

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())
    
    def __init__(self, *args, **kwargs):  # we want to put the values in the agent dynamically.
        user = kwargs.pop('request').user
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        
        self.fields["agent"].queryset = Agent.objects.filter(organization=user.userprofile)
        

class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('category',)
        
        
class SignupModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')