from django.contrib import admin

# Register your models here.
from registration.models import *


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Kişisel bilgiler', {'fields': ['trainer', 'user', 'phone', 'avatar']}),
        ('Adres bilgileri', {'fields': ['address']}),
    ]
    list_display = ['user', 'phone', 'address']
    list_display_links = ['user']
    # list_filter = ['user']  # Burada yazdığımız alana göre filtreleme işlemi yapar
    search_fields = ['user__username']  # Arama alanı eklediğiniz alanlar içinde arama yapar

    class Meta:
        model = Personal


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Kişisel bilgiler', {'fields': ['corporate', 'user', 'phone', 'avatar']}),
        ('Adres bilgileri', {'fields': ['address']}),
    ]
    list_display = ['user', 'phone', 'address']
    list_display_links = ['user']
    # list_filter = ['user']  # Burada yazdığımız alana göre filtreleme işlemi yapar
    search_fields = ['user__username']  # Arama alanı eklediğiniz alanlar içinde arama yapar

    class Meta:
        model = Trainer


@admin.register(Corporate)
class CorporateAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Kurum bilgileri', {'fields': ['corporate_name', 'phone', 'logo']}),
        ('Yetkili bilgileri', {'fields': ['user', 'authorized_task']}),
        ('Adres bilgileri', {'fields': ['address']}),
    ]
    list_display = ['corporate_name', 'authorized_task', 'phone',
                    'address']  # Admin arayüzünde görünecek sutunları buraya yazıyoruz
    list_display_links = [
        'corporate_name']  # Admin arayuzunde görünecek sutunların hangisine link vermek istiyorsak o sutunun adını buraya ekliyoruz
    list_filter = ['corporate_name']  # Burada yazdığımız alana göre filtreleme işlemi yapar
    search_fields = ['corporate_name']  # Arama alanı eklediğiniz alanlar içinde arama yapar

    class Meta:
        model = Corporate
