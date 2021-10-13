from django import forms

from pilates.models import personalTrainingInput1, personalTrainingInput2, personalTrainingInput3, \
    personalTrainingInput4


class PersonalTrainingForm1(forms.ModelForm):
    class Meta:
        model = personalTrainingInput1
        fields = "__all__"


class PersonalTrainingForm2(forms.ModelForm):
    class Meta:
        model = personalTrainingInput2
        fields = "__all__"


class PersonalTrainingForm3(forms.ModelForm):
    class Meta:
        model = personalTrainingInput3
        fields = "__all__"


class PersonalTrainingForm4(forms.ModelForm):
    class Meta:
        model = personalTrainingInput4
        fields = "__all__"
