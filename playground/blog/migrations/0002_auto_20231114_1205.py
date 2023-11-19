# Generated by Django 2.2.28 on 2023-11-14 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id_equip', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('disponibilite', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Membres',
            fields=[
                ('id_membre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('etat', models.CharField(max_length=20)),
                ('lateralite', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('photo', models.CharField(max_length=200)),
                ('lieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Equipement')),
            ],
        ),
        migrations.DeleteModel(
            name='Billet',
        ),
    ]
