from django.contrib import admin
from .models import KorisnickiProfil, FitnessCilj, Vjezba
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(KorisnickiProfil)
class KorisnickiProfilAdmin(admin.ModelAdmin):
    list_display = ('korisnik', 'godine', 'visina', 'tezina')
    search_fields = ('korisnik__username',)

@admin.register(FitnessCilj)
class FitnessCiljAdmin(admin.ModelAdmin):
    list_display = ('korisnik', 'naziv_cilja', 'ciljna_vrijednost', 'trenutna_vrijednost', 'rok')
    search_fields = ('korisnik__korisnik__username', 'naziv_cilja')

@admin.register(Vjezba)
class VjezbaAdmin(admin.ModelAdmin):
    list_display = ('naziv_vjezbe', 'trajanje', 'potrosene_kalorije', 'video_url', 'prikazi_korisnike')
    list_filter = ('naziv_vjezbe', 'trajanje', 'potrosene_kalorije')
    search_fields = ('naziv_vjezbe',)

    def prikazi_korisnike(self, obj):
        return ", ".join([korisnik.korisnik.username for korisnik in obj.korisnici.all()])
    prikazi_korisnike.short_description = 'Korisnici'

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)