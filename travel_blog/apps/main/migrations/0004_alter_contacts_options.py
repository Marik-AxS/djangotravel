# Generated by Django 5.0.7 on 2024-08-15 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контактный', 'verbose_name_plural': 'Контактная'},
        ),
    ]
