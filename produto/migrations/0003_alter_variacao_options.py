# Generated by Django 5.0.1 on 2024-01-26 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_variacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variacao',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
    ]
