from django import forms
from .models import Invitation


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = '__all__'

        exclude = ['from_user']
