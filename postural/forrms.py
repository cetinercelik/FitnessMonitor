from django import forms

from postural.models import PosturInputs


class PosturalForm(forms.ModelForm):
    class Meta:
        model = PosturInputs
        fields ="__all__"