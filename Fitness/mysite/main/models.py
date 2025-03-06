from django.db import models
from django.contrib.auth.models import User

class KorisnickiProfil(models.Model):
    korisnik = models.OneToOneField(User, on_delete=models.CASCADE)
    godine = models.PositiveIntegerField()
    visina = models.FloatField(help_text="Visina u cm")
    tezina = models.FloatField(help_text="Težina u kg")
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.korisnik.username

class FitnessCilj(models.Model):
    FITNESS_CILJ = [
        ('Mršavljenje', 'Mršavljenje'),
        ('Dobivanje mišićne mase', 'Dobivanje mišićne mase'),
        ('Izdržljivost', 'Izdržljivost'),
        ('Fleksibilnost', 'Fleksibilnost'),
        ('Snaga', 'Snaga'),
        ('Brzina', 'Brzina')
    ]
    korisnik = models.ForeignKey(KorisnickiProfil, on_delete=models.CASCADE, related_name="fitness_ciljevi")
    naziv_cilja = models.CharField(max_length=255, choices=FITNESS_CILJ)
    ciljna_vrijednost = models.FloatField(default=0, help_text="(npr. ciljna težina, udaljenost ili broj ponavljanja)")
    trenutna_vrijednost = models.FloatField(default=0)
    rok = models.DateField()

    def __str__(self):
        return f"{self.naziv_cilja} ({self.korisnik.korisnik.username})"

class Vjezba(models.Model):
    korisnici = models.ManyToManyField(KorisnickiProfil, related_name="odabrane_vjezbe", blank=True)
    naziv_vjezbe = models.CharField(max_length=100)
    trajanje = models.PositiveIntegerField(blank=True, null=True)
    potrosene_kalorije = models.PositiveIntegerField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.naziv_vjezbe}"