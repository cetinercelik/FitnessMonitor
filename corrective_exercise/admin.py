from django.contrib import admin

# Register your models here.
from corrective_exercise.models import corrective_exercise


@admin.register(corrective_exercise)
class corrective_exerciseAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = corrective_exercise
