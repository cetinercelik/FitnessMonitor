from django import forms

from athletic_development.models import athletticDev_inputs


class AthleticDevForm(forms.ModelForm):
    class Meta:
        model = athletticDev_inputs
        fields = "__all__"