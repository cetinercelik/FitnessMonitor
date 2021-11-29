from django.contrib import admin

# Register your models here.
from athletic_development.models import athleticDev_subTitle, athDev_mainTitle, ath_property


@admin.register(athDev_mainTitle)
class MainTitleAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

    class Meta:
        model = athDev_mainTitle
        verbose_name = 'Ana Başlıklar'


@admin.register(athleticDev_subTitle)
class SubTitleAdmin(admin.ModelAdmin):
    list_display = ['sub_title']
    list_display_links = ['sub_title']

    class Meta:
        model = athleticDev_subTitle
        verbose_name = 'Alt Başlıklar'


@admin.register(ath_property)
class Ath_propertyAdmin(admin.ModelAdmin):
    list_display = ['subtitle']
    list_display_links = ['subtitle']

    class Meta:
        model = ath_property
        verbose_name = 'Alt Başlıklar'

#
# @admin.register(athletticDev_inputs)
# class AthleticInputsAdmin(admin.ModelAdmin):
#     list_display = ['personal', 'trainer', 'date']
#     list_filter = ['trainer', 'personal']
#     search_fields = ['personal__user__first_name',
#                      'personal__user__last_name',
#                      'trainer__user__first_name',
#                      'trainer__user__last_name']
#
#     class Meta:
#         model = athletticDev_inputs
#         verbose_name = 'Atletik Performans Gelişim  Inputs'
