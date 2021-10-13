from django.contrib import admin

from athletic.models import AthleticInpt


@admin.register(AthleticInpt)
class AthleticInputsAdmin(admin.ModelAdmin):
    list_display = ['personal', 'trainer', 'date']
    list_filter = ['trainer', 'personal']
    search_fields = ['personal__user__first_name',
                     'personal__user__last_name',
                     'trainer__user__first_name',
                     'trainer__user__last_name']

    class Meta:
        model = AthleticInpt
