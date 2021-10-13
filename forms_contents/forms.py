from django import forms

from forms_contents.models import InterviewInput, ContractInput, VoluntaryInput, FamilyInput, \
    ExercisehistoryInput, \
    ParqInput, MoodInput, SleepqualityInput, NutritionInput, EudaimoniaInput, MedikalInpt, CurriculumWalking1, \
    CurriculumMorning, CurriculumNoon, CurriculumEvening, CurriculumSnack


# Ön görüşme Formu
class InterviewForm(forms.ModelForm):
    class Meta:
        model = InterviewInput
        fields = "__all__"


# Teklif ve Sözleşme Formu
class ContractForm(forms.ModelForm):
    class Meta:
        model = ContractInput
        fields = "__all__"


# Medikal izin Formu

class MedikalForm(forms.ModelForm):
    class Meta:
        model = MedikalInpt
        fields = "__all__"


# Gönüllü  Rıza Formu
class VoluntaryForm(forms.ModelForm):
    class Meta:
        model = VoluntaryInput
        fields = "__all__"


# Aile Öyküsü ve Hastalık Geçmişi
class FamilyForm(forms.ModelForm):
    class Meta:
        model = FamilyInput
        fields = "__all__"


# Egzersiz Geçmişi ve Yönelimi
class ExercisehistoryForm(forms.ModelForm):
    class Meta:
        model = ExercisehistoryInput
        fields = "__all__"


# 7.PAR-Q Formu
class ParqForm(forms.ModelForm):
    class Meta:
        model = ParqInput
        fields = "__all__"


# Duygu Durumu – Sosyalite – İş Koşulları Formu
class MoodForm(forms.ModelForm):
    class Meta:
        model = MoodInput
        fields = "__all__"


# Uyku Kalitesi – Zindelik – Ağrı Durumu Formu
class SleepqualityForm(forms.ModelForm):
    class Meta:
        model = SleepqualityInput
        fields = "__all__"


# Beslenme ve Tüketim Alışkanlıkları Formu
class NutritionForm(forms.ModelForm):
    class Meta:
        model = NutritionInput
        fields = "__all__"



# Eudaimonia Sağlıklı Yaşam Semptom Formu
class EudaimoniaForm(forms.ModelForm):
    class Meta:
        model = EudaimoniaInput
        fields = "__all__"


# İzlence Formu Yürüme Mesafesi
class CurriculumWalkingForm(forms.ModelForm):
    class Meta:
        model = CurriculumWalking1
        fields = "__all__"

# İzlence Formu Sabah Öğünü
class CurriculumMorningForm(forms.ModelForm):
    class Meta:
        model = CurriculumMorning
        fields = "__all__"

# İzlence Formu Öğle Öğünü
class CurriculumNoonForm(forms.ModelForm):
    class Meta:
        model = CurriculumNoon
        fields = "__all__"


# İzlence Formu Akşam Öğünü
class CurriculumEveningForm(forms.ModelForm):
    class Meta:
        model = CurriculumEvening
        fields = "__all__"


# İzlence Formu Akşam Öğünü
class CurriculumSnackForms(forms.ModelForm):
    class Meta:
        model = CurriculumSnack
        fields = "__all__"