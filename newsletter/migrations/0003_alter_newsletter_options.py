# Generated by Django 5.1.3 on 2024-12-05 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_message_owner_newsletter_owner_recipient_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ['start_mail'], 'permissions': [('set_active', 'Set active')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]
