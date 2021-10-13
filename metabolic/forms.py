from django import forms

from metabolic.models import Metabolic, Metabolic2


class MetabolicForms(forms.ModelForm):
    class Meta:
        model = Metabolic
        fields = "__all__"


class MetabolicForms2(forms.ModelForm):
    class Meta:
        model = Metabolic2
        fields = "__all__"

