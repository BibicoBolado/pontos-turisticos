# Generated by Django 2.0.1 on 2018-06-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('pontos', '0005_pontos_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontos',
            name='avaliacao',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]
