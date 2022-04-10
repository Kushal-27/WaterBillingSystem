from django import forms
from accounts.models import Users

class userforms(forms.ModelForm):
    class meta:
        model=Users
        fields='__all__'