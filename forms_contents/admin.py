from django.contrib import admin

# Register your models here.
from forms_contents.models import InterviewInput, ContractInput, MedikalInpt, VoluntaryInput, FamilyInput, \
    ExercisehistoryInput, ParqInput, MoodInput, SleepqualityInput, NutritionInput, EudaimoniaInput


@admin.register(InterviewInput)
class InterviewInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = InterviewInput


@admin.register(ContractInput)
class ContractInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = ContractInput


@admin.register(MedikalInpt)
class MedikalInptsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = MedikalInpt


@admin.register(VoluntaryInput)
class VoluntaryInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = VoluntaryInput


@admin.register(FamilyInput)
class FamilyInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = FamilyInput


@admin.register(ExercisehistoryInput)
class ExercisehistoryInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = ExercisehistoryInput


@admin.register(ParqInput)
class ParqInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = ParqInput


@admin.register(MoodInput)
class MoodInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = MoodInput


@admin.register(SleepqualityInput)
class SleepqualityInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = SleepqualityInput


@admin.register(NutritionInput)
class NutritionInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = NutritionInput


@admin.register(EudaimoniaInput)
class EudaimoniaInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = EudaimoniaInput

#
# @admin.register(CurriculumInput)
# class CurriculumInputsAdmin(admin.ModelAdmin):
#     list_display = ['personal', 'trainer']
#     list_filter = ['trainer', 'personal']
#     search_fields = ['personal__user__first_name',
#                      'personal__user__last_name',
#                      'trainer__user__first_name',
#                      'trainer__user__last_name']
#
#     class Meta:
#         model = CurriculumInput
