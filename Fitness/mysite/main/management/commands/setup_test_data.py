from django.core.management.base import BaseCommand
from django.db import transaction
import random
from main.models import KorisnickiProfil, FitnessCilj, Vjezba
from main.factories import KorisnickiProfilFactory, FitnessCiljFactory, VjezbaFactory
from django.contrib.auth.models import User

NUM_KORISNIKA = 5
MIN_CILJEVA_PO_KORISNIKU = 1
MAX_CILJEVA_PO_KORISNIKU = 3
MIN_VJEZBI_PO_KORISNIKU = 3
MAX_VJEZBI_PO_KORISNIKU = 8

class Command(BaseCommand):
    help = "Generira testne podatke za fitness aplikaciju"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write('Započinjem brisanje starih podataka...')
        
        models = [Vjezba, FitnessCilj, KorisnickiProfil, User]
        for m in models:
            m.objects.all().delete()

        self.stdout.write('Kreiram nove podatke...')
        
        try:
            self.stdout.write(f'Kreiram {NUM_KORISNIKA} korisnika s profilima...')
            for i in range(NUM_KORISNIKA):
                profil = KorisnickiProfilFactory()
                
                broj_ciljeva = random.randint(MIN_CILJEVA_PO_KORISNIKU, MAX_CILJEVA_PO_KORISNIKU)
                self.stdout.write(f'Kreiram {broj_ciljeva} ciljeva za korisnika {profil.korisnik.username}...')
                for _ in range(broj_ciljeva):
                    FitnessCiljFactory(korisnik=profil)
                
                broj_vjezbi = random.randint(MIN_VJEZBI_PO_KORISNIKU, MAX_VJEZBI_PO_KORISNIKU)
                self.stdout.write(f'Kreiram {broj_vjezbi} vježbi za korisnika {profil.korisnik.username}...')
                for _ in range(broj_vjezbi):
                    VjezbaFactory(korisnik=profil)
            
            self.stdout.write(self.style.SUCCESS('Uspješno kreirani testni podaci!'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Greška prilikom kreiranja podataka: {str(e)}'))
            raise e