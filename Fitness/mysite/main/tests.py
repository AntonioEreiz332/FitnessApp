from django.test import TestCase
from django.contrib.auth.models import User
from .models import KorisnickiProfil, FitnessCilj, Vjezba
from django.core.exceptions import ValidationError
from django.utils import timezone

class KorisnickiProfilModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='testuser@example.com'
        )
        self.korisnicki_profil = KorisnickiProfil.objects.create(
            korisnik=self.user,
            godine=25,
            visina=180.5,
            tezina=80.0,
            opis='Testni korisnički profil'
        )

    def test_korisnicki_profil_creation(self):
        self.assertTrue(isinstance(self.korisnicki_profil, KorisnickiProfil))
        self.assertEqual(self.korisnicki_profil.korisnik.username, 'testuser')
        self.assertEqual(self.korisnicki_profil.godine, 25)
        self.assertEqual(self.korisnicki_profil.visina, 180.5)
        self.assertEqual(self.korisnicki_profil.tezina, 80.0)
        self.assertEqual(str(self.korisnicki_profil), 'testuser')

class FitnessCiljModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='testuser@example.com'
        )
        self.korisnicki_profil = KorisnickiProfil.objects.create(
            korisnik=self.user,
            godine=25,
            visina=180.5,
            tezina=80.0
        )
        self.fitness_cilj = FitnessCilj.objects.create(
            korisnik=self.korisnicki_profil,
            naziv_cilja='Mršavljenje',
            ciljna_vrijednost=75.0,
            trenutna_vrijednost=80.0,
            rok=timezone.now().date()
        )

    def test_fitness_cilj_creation(self):
        self.assertTrue(isinstance(self.fitness_cilj, FitnessCilj))
        self.assertEqual(self.fitness_cilj.naziv_cilja, 'Mršavljenje')
        self.assertEqual(self.fitness_cilj.ciljna_vrijednost, 75.0)
        self.assertEqual(self.fitness_cilj.trenutna_vrijednost, 80.0)
        self.assertEqual(str(self.fitness_cilj), 'Mršavljenje (testuser)')

    def test_fitness_cilj_korisnik_relationship(self):
        self.assertEqual(self.fitness_cilj.korisnik, self.korisnicki_profil)
        self.assertTrue(self.fitness_cilj in self.korisnicki_profil.fitness_ciljevi.all())

class VjezbaModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='testuser@example.com'
        )
        self.korisnicki_profil = KorisnickiProfil.objects.create(
            korisnik=self.user,
            godine=25,
            visina=180.5,
            tezina=80.0
        )
        self.vjezba = Vjezba.objects.create(
            naziv_vjezbe='Trčanje',
            trajanje=30,
            potrosene_kalorije=300,
            video_url='https://www.youtube.com/watch?v=test'
        )
        self.vjezba.korisnici.add(self.korisnicki_profil)

    def test_vjezba_creation(self):
        self.assertTrue(isinstance(self.vjezba, Vjezba))
        self.assertEqual(self.vjezba.naziv_vjezbe, 'Trčanje')
        self.assertEqual(self.vjezba.trajanje, 30)
        self.assertEqual(self.vjezba.potrosene_kalorije, 300)
        self.assertEqual(str(self.vjezba), 'Trčanje')

    def test_vjezba_korisnici_relationship(self):
        self.assertTrue(self.korisnicki_profil in self.vjezba.korisnici.all())
        self.assertTrue(self.vjezba in self.korisnicki_profil.odabrane_vjezbe.all())