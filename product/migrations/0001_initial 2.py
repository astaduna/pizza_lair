# Generated by Django 4.2.1 on 2023-05-05 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sides', '0002_side_allergens'),
        ('pizza', '0003_remove_pizza_price_pizza_allergens_pizza_large_price_and_more'),
        ('sauces', '0001_initial'),
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('drinks', models.ManyToManyField(blank=True, related_name='offers_drinks', to='drinks.drink')),
                ('pizzas', models.ManyToManyField(blank=True, related_name='offers_pizzas', to='pizza.pizza')),
                ('sauce', models.ManyToManyField(blank=True, related_name='offers_drinks', to='sauces.sauce')),
                ('sides', models.ManyToManyField(blank=True, related_name='offers_sides', to='sides.side')),
            ],
        ),
    ]
