from django.contrib import admin

# Register your models here.
from settings.models import homemodel, ImagePost, Team, Blog, About, FitnessMonitor, Founder, SocialMedia, \
    Sub_Philosophy, Philosophy, Corporate_solve, Sub_Pricing, Pricing, sendMessage


class SocialMediaAdmin(admin.StackedInline):
    model = SocialMedia
    extra = 1


class Sub_PhilosophyAdmin(admin.StackedInline):
    model = Sub_Philosophy


# @admin.register(SocialMedia)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(homemodel)
class HomepageAdmin(admin.ModelAdmin):
    # inlines = [SocialMediaAdmin]
    fieldsets = [
        ('Kurucu bilgileri',
         {'fields': ['corporate_logo']}),
        ('Ana Başlık bilgileri',
         {'fields': ['corporate_main_title', 'software_main_title', 'blog_main_title', 'team_main_title']}),
        ('Merkez Ofis bilgileri',
         {'fields': ['central_phone', 'central_address', 'central_local_link']}),
        ('Şube Ofis bilgileri', {'fields': ['branch_phone', 'branch_adress', 'branch_local_link']}),
        ('Kurum Sosyal Medya Linkleri', {'fields': ['instagram', 'twitter', 'facebook', 'mail']}),
    ]
    list_display = ['corporate_main_title']
    list_display_links = ['corporate_main_title']

    # Admin Kısmında yeni veri ekleme butonununu Kapatır
    def has_add_permission(self, request):
        return False

    # Silme Butonunu Kaldırı yalnızca veri Üzerinde Guncelleme Yapabilirsin
    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = homemodel
        verbose_name = "Anasayfa Bilgileri"


@admin.register(ImagePost)
class ImagePostAdmin(admin.ModelAdmin):
    list_display = ['main_title']
    list_display_links = ['main_title']

    class Meta:
        model = ImagePost
        verbose_name = 'Slider İçerik Ekle'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    # inlines = [SocialMediaAdmin]
    list_display = ['name_surname', 'job']
    list_display_links = ['name_surname']

    class Meta:
        model = Team
        verbose_name = 'Ekip Bilgilerini Ekle'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_title', 'blog_date']
    list_display_links = ['blog_title']

    class Meta:
        model = Blog
        verbose_name = 'Blog Haberleri Ekle'


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

    # Admin Kısmında yeni veri ekleme butonununu Kapatır
    def has_add_permission(self, request):
        return False

    # Silme Butonunu Kaldırı yalnızca veri Üzerinde Guncelleme Yapabilirsin
    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = About
        verbose_name = 'Hakkımzda Alanı Bilgileri'


@admin.register(FitnessMonitor)
class FitnessMonitorAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

    class Meta:
        model = FitnessMonitor
        verbose_name = 'FitnessMonitor Keşfet Alanı Bilgileri'


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    # inlines = [SocialMediaAdmin]
    list_display = ['founder_name_surname']
    list_display_links = ['founder_name_surname']
    extra = 1

    # Admin Kısmında yeni veri ekleme butonununu Kapatır
    def has_add_permission(self, request):
        return False

    # Silme Butonunu Kaldırı yalnızca veri Üzerinde Guncelleme Yapabilirsin
    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = Founder
        verbose_name = 'Kurucu Alanı Bilgileri'


@admin.register(Corporate_solve)
class Corporate_solveAdmin(admin.ModelAdmin):
    list_display = ['main_title']
    list_display_links = ['main_title']

    # Admin Kısmında yeni veri ekleme butonununu Kapatır
    def has_add_permission(self, request):
        return False

    # Silme Butonunu Kaldırı yalnızca veri Üzerinde Guncelleme Yapabilirsin
    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = Corporate_solve
        verbose_name = 'Kurumsal Çözümlemeler Alanı Bilgileri'


@admin.register(Philosophy)
class PhilosophyAdmin(admin.ModelAdmin):
    inlines = [Sub_PhilosophyAdmin]
    list_display = ['title']
    list_display_links = ['title']

    # Admin Kısmında yeni veri ekleme butonununu Kapatır
    def has_add_permission(self, request):
        return False

    # Silme Butonunu Kaldırı yalnızca veri Üzerinde Guncelleme Yapabilirsin
    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = Philosophy
        verbose_name = 'Felsefe Alanı Bilgileri'


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    # inlines = [Sub_PricingAdmin]
    list_display = ['title']
    list_display_links = ['title']

    class Meta:
        model = Pricing
        verbose_name = 'Fiyatlandırma Alan Bilgileri'


@admin.register(Sub_Pricing)
class Sub_PricingAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

    class Meta:
        model = Sub_Pricing
        verbose_name = 'FitnessMonitor Paneli Fiyatlandırma Altbaşlıkları'

@admin.register(sendMessage)
class sendMessageAdmin(admin.ModelAdmin):
    list_display = ['name_surname','mail','subject']
    list_display_links = ['name_surname']

    # Admin Kısmında yeni veri ekleme butonununu Kapatır
    def has_add_permission(self, request):
        return False

    # Güncelleme Butonunu Kaldırı yalnızca veri Üzerinde Guncelleme Yapabilirsin
    def has_update_permission(self, request):
        return False


    class Meta:
        model = sendMessage
        verbose_name = 'Kullanıcı Mesajları'