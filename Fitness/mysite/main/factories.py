import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from main.models import KorisnickiProfil, FitnessCilj, Vjezba
from datetime import date, timedelta
import random

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'test_user_{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')

class KorisnickiProfilFactory(DjangoModelFactory):
    class Meta:
        model = KorisnickiProfil

    korisnik = factory.SubFactory(UserFactory)
    godine = factory.LazyFunction(lambda: random.randint(18, 60))
    visina = factory.LazyFunction(lambda: round(random.uniform(160, 200), 2))
    tezina = factory.LazyFunction(lambda: round(random.uniform(50, 100), 2))
    opis = factory.LazyAttribute(lambda obj: f'Ovo je testni profil korisnika {obj.korisnik.username}')

class FitnessCiljFactory(DjangoModelFactory):
    class Meta:
        model = FitnessCilj

    korisnik = factory.SubFactory(KorisnickiProfilFactory)
    naziv_cilja = factory.LazyFunction(
        lambda: random.choice(['Smanjenje težine', 'Povećanje snage', 'Izdržljivost'])
    )
    ciljna_vrijednost = factory.LazyFunction(lambda: round(random.uniform(60, 90), 2))
    trenutna_vrijednost = factory.LazyFunction(lambda: round(random.uniform(50, 80), 2))
    rok = factory.LazyFunction(
        lambda: date.today() + timedelta(days=random.randint(30, 180))
    )

class VjezbaFactory(DjangoModelFactory):
    class Meta:
        model = Vjezba

    korisnik = factory.SubFactory(KorisnickiProfilFactory)
    naziv_vjezbe = factory.LazyFunction(
        lambda: random.choice(['Trčanje', 'Bicikl', 'Teretana', 'Plivanje'])
    )
    trajanje = factory.LazyFunction(lambda: random.randint(30, 120))
    potrosene_kalorije = factory.LazyFunction(lambda: round(random.uniform(200, 800), 2))
    datum = factory.LazyFunction(
        lambda: date.today() - timedelta(days=random.randint(0, 30))
    )