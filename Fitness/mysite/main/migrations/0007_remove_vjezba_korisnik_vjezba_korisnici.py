# Generated by Django 5.1.2 on 2025-03-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_vjezba_naziv_vjezbe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vjezba',
            name='korisnik',
        ),
        migrations.AddField(
            model_name='vjezba',
            name='korisnici',
            field=models.ManyToManyField(blank=True, related_name='odabrane_vjezbe', to='main.korisnickiprofil'),
        ),
    ]
