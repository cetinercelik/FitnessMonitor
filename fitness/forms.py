from django import forms

from fitness.models import FitnessInputs


class FitnessForm(forms.ModelForm):
    class Meta:
        model = FitnessInputs
        fields = "__all__"
