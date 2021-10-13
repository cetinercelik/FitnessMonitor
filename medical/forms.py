from django import forms

from medical.models import MedicalInputModel1, MedicalInputModel2


class MedicalForm(forms.ModelForm):
    class Meta:
        model = MedicalInputModel1
        fields = '__all__'


class MedicalForm2(forms.ModelForm):
    class Meta:
        model = MedicalInputModel2
        fields = '__all__'
