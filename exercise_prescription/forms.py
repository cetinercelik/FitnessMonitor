from django import forms

from exercise_prescription.models import exercise_prescription, exercise_prescription_level, exercise_prescripion_chest, \
    exercise_prescription_shoulder, exercise_prescription_back, exercise_prescription_biseps, \
    exercise_prescription_triseps, exercise_prescription_gluteal, exercise_prescription_kuadriseps, \
    exercise_prescription_hamstring, exercise_prescription_gastrocnemius, exercise_prescription_core


class Exercise_prescriptionForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription
        fields = "__all__"


class exercise_prescription_levelForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_level
        fields = "__all__"


class exercise_prescripion_chestForm(forms.ModelForm):
    class Meta:
        model = exercise_prescripion_chest
        fields = "__all__"


class exercise_prescription_shoulderForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_shoulder
        fields = "__all__"


class exercise_prescription_backForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_back
        fields = "__all__"


class exercise_prescription_bisepsForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_biseps
        fields = "__all__"


class exercise_prescription_trisepsForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_triseps
        fields = "__all__"


class exercise_prescription_glutealForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_gluteal
        fields = "__all__"


class exercise_prescription_kuadrisepsForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_kuadriseps
        fields = "__all__"


class exercise_prescription_hamstringForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_hamstring
        fields = "__all__"


class exercise_prescription_gastrocnemiusForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_gastrocnemius
        fields = "__all__"


class exercise_prescription_coreForm(forms.ModelForm):
    class Meta:
        model = exercise_prescription_core
        fields = "__all__"
