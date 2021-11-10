from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from registration.models import *

# Unregister the provided model admin
admin.site.unregister(User)


# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    readonly_fields = ('personal_image_admin',)
    fieldsets = [
        ('Kişisel bilgiler', {'fields': ['personal_image_admin', 'avatar', 'trainer', 'user', 'phone', 'gender']}),
        ('Adres bilgileri', {'fields': ['address']}),
    ]
    list_display = ['personal_image_admin', 'user', 'phone', 'address']
    list_display_links = ['user']
    # list_filter = ['user']  # Burada yazdığımız alana göre filtreleme işlemi yapar
    search_fields = ['user__username']  # Arama alanı eklediğiniz alanlar içinde arama yapar

    def personal_image_admin(self, obj):
        return obj.personal_image_admin

    personal_image_admin.short_description = 'Fotoğraf'
    personal_image_admin.allow_tags = True

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
        ('Kurum bilgileri', {'fields': ['logo', 'corporate_name', 'phone']}),
        ('Yetkili bilgileri', {'fields': ['authorized_image', 'user', 'authorized_task']}),
        ('Adres bilgileri', {'fields': ['address']}),
    ]
    list_display = ['corporate_name', 'authorized_task', 'phone',
                    'address']  # Admin arayüzünde görünecek sutunları buraya yazıyoruz
    list_display_links = [
        'corporate_name']  # Admin arayuzunde görünecek sutunların hangisine link vermek istiyorsak o sutunun adını buraya ekliyoruz
    list_filter = ['corporate_name']  # Burada yazdığımız alana göre filtreleme işlemi yapar
    search_fields = ['corporate_name']  # Arama alanı eklediğiniz alanlar içinde arama yapar

    def corporate_logo_admin(self, obj):
        return obj.corporate_logo_admin

    corporate_logo_admin.short_description = 'Kurum Logosu'
    corporate_logo_admin.allow_tags = True

    def authorized_image_admin(self, obj):
        return obj.authorized_image_admin

    authorized_image_admin.short_description = 'Kurum Logosu'
    authorized_image_admin.allow_tags = True

    class Meta:
        model = Corporate
