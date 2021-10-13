from django import forms

from athletic.models import AthleticInpt


class AthleticForm(forms.ModelForm):
    class Meta:
        model = AthleticInpt
        fields = "__all__"
