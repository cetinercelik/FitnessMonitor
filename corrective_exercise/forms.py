from django import forms

from corrective_exercise.models import corrective_exercise, corrective_exercise2, corrective_exercise3, \
    corrective_exercise4


class Corrective_exercise(forms.ModelForm):
    class Meta:
        model = corrective_exercise
        fields = "__all__"


class Corrective_exercise2(forms.ModelForm):
    class Meta:
        model = corrective_exercise2
        fields = "__all__"

class Corrective_exercise3(forms.ModelForm):
    class Meta:
        model = corrective_exercise3
        fields = "__all__"

class Corrective_exercise4(forms.ModelForm):
    class Meta:
        model = corrective_exercise4
        fields = "__all__"
