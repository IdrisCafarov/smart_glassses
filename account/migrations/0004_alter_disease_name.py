# Generated by Django 4.1.6 on 2023-02-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_myuser_usertype_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.CharField(choices=[('Insomnia', 'Insomnia'), ('Diabet', 'Diabet'), ('Heart Attack', 'Heart Attack'), ('Being Nihad', 'Being Nihad')], max_length=50, null=True, verbose_name='Choose your Diseases'),
        ),
    ]
