# Generated by Django 4.2.1 on 2023-05-10 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='SauceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('sauce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sauces.sauce')),
            ],
        ),
    ]
