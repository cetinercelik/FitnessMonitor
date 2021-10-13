from django.contrib import admin

# Register your models here.
from exercise_prescription.models import exercise_prescription


@admin.register(exercise_prescription)
class exercise_prescriptionAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = exercise_prescription