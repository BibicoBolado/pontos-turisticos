# Generated by Django 2.0.1 on 2018-06-06 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha1', models.CharField(max_length=150)),
                ('linha2', models.CharField(blank=True, max_length=150, null=True)),
                ('cidade', models.CharField(max_length=150)),
                ('estado', models.CharField(max_length=150)),
                ('pais', models.CharField(max_length=150)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
