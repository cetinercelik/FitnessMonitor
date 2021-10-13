from django import forms

from medical_exercise.models import medical_exercise1, medical_exercise2, medical_exercise3, medical_exercise4, \
    medical_exercise5, medical_exercise6, medical_exercise7, medical_exercise8, medical_exercise9, medical_exercise10, \
    medical_exercise11, medical_exercise12, medical_exercise13


class MedicalExerciseForm1(forms.ModelForm):
    class Meta:
        model = medical_exercise1
        fields = "__all__"


class MedicalExerciseForm2(forms.ModelForm):
    class Meta:
        model = medical_exercise2
        fields = "__all__"


class MedicalExerciseForm3(forms.ModelForm):
    class Meta:
        model = medical_exercise3
        fields = "__all__"


class MedicalExerciseForm4(forms.ModelForm):
    class Meta:
        model = medical_exercise4
        fields = "__all__"


class MedicalExerciseForm5(forms.ModelForm):
    class Meta:
        model = medical_exercise5
        fields = "__all__"


class MedicalExerciseForm6(forms.ModelForm):
    class Meta:
        model = medical_exercise6
        fields = "__all__"


class MedicalExerciseForm7(forms.ModelForm):
    class Meta:
        model = medical_exercise7
        fields = "__all__"


class MedicalExerciseForm8(forms.ModelForm):
    class Meta:
        model = medical_exercise8
        fields = "__all__"


class MedicalExerciseForm9(forms.ModelForm):
    class Meta:
        model = medical_exercise9
        fields = "__all__"


class MedicalExerciseForm10(forms.ModelForm):
    class Meta:
        model = medical_exercise10
        fields = "__all__"


class MedicalExerciseForm11(forms.ModelForm):
    class Meta:
        model = medical_exercise11
        fields = "__all__"


class MedicalExerciseForm12(forms.ModelForm):
    class Meta:
        model = medical_exercise12
        fields = "__all__"


class MedicalExerciseForm13(forms.ModelForm):
    class Meta:
        model = medical_exercise13
        fields = "__all__"
