# Generated by Django 5.1.3 on 2024-12-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_try'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipient',
            name='name',
        ),
        migrations.AddField(
            model_name='recipient',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Почта получателя'),
        ),
    ]
