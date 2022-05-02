from django import forms
from accounts.models import Users

class userforms(forms.ModelForm):
    class Meta:
        model=Users
        fields='__all__'