# Generated by Django 4.0.5 on 2022-07-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20180417_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]