# Generated by Django 3.2.4 on 2021-06-10 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_messageform_contactform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='MessageForm',
            new_name='message',
        ),
    ]