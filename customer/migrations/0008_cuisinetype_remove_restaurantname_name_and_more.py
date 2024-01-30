# Generated by Django 5.0.1 on 2024-01-30 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_restaurantname'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuisineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurantname',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='restaurantname',
            name='products',
        ),
        migrations.AddField(
            model_name='restaurantname',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='restaurantname',
            name='website',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='restaurantname',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='restaurantname',
            name='type',
            field=models.ManyToManyField(related_name='type', to='customer.cuisinetype'),
        ),
        migrations.AddField(
            model_name='restaurantname',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
