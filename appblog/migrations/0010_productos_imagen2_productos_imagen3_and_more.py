# Generated by Django 4.0.5 on 2022-08-11 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0009_delete_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='imagen2',
            field=models.ImageField(blank=True, null=True, upload_to='imgproductos'),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen3',
            field=models.ImageField(blank=True, null=True, upload_to='imgproductos'),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen4',
            field=models.ImageField(blank=True, null=True, upload_to='imgproductos'),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen5',
            field=models.ImageField(blank=True, null=True, upload_to='imgproductos'),
        ),
        migrations.AddField(
            model_name='productos',
            name='imagen6',
            field=models.ImageField(blank=True, null=True, upload_to='imgproductos'),
        ),
    ]
