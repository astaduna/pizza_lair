# Generated by Django 4.2.1 on 2023-05-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='side',
            name='allergens',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
