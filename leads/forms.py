from django import forms
from django.core.exceptions import ValidationError
from .models import Lead, Agent, User, Followup

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "first_name",
            "second_name",
            "age",
            "agent",
            "category",
            "description",
            "phone_number",
            "email",
            'profile_image',
        )
    
    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if data != 'Abdulrahman':
    #         raise ValidationError('Your name is not Abdulrahman')
    #     return data
    
    # def clean(self):
    #     first_name = self.cleaned_data['first_name']
    #     second_name = self.cleaned_data['second_name']
    #     if f'{first_name} {second_name}' != 'Abdulrahman Diab':
    #         raise ValidationError('Your full name is not Abdulrahman Diab')
        


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


class FollowupCreateForm(forms.ModelForm):
    class Meta:
        model = Followup
        fields = (
            'notes',
            'file',
        )     
        