# forms.py
from django import forms

from accounts.models import UserService

class ServiceAddForm(forms.ModelForm):
    class Meta:
        model = UserService
        fields = ('service', 'username')

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

