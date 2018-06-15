# Generated by Django 2.0.1 on 2018-06-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pontos', '0007_pontos_localizcao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontos',
            name='atracoes',
            field=models.ManyToManyField(blank=True, null=True, to='atracoes.Atracoes'),
        ),
        migrations.AlterField(
            model_name='pontos',
            name='avaliacao',
            field=models.ManyToManyField(blank=True, null=True, to='avaliacoes.Avaliacao'),
        ),
        migrations.AlterField(
            model_name='pontos',
            name='comentario',
            field=models.ManyToManyField(blank=True, null=True, to='comentarios.Comentario'),
        ),
    ]