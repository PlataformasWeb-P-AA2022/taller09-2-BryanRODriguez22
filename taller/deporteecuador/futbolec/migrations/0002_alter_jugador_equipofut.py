# Generated by Django 4.0.5 on 2022-06-15 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futbolec', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='equipofut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elquipo', to='futbolec.equipo'),
        ),
    ]
