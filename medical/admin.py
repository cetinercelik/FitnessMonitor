from django.contrib import admin

# Register your models here.
from medical.models import MedicalInputModel1


@admin.register(MedicalInputModel1)
class MedicalInputsAdmin(admin.ModelAdmin):

    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = MedicalInputModel1