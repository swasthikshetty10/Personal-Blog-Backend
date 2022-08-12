# Generated by Django 3.2.4 on 2021-06-27 15:43

from django.db import migrations
import main_app.Utility.formatChecker


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_projectrequests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectrequests',
            name='user',
        ),
        migrations.AlterField(
            model_name='projectrequests',
            name='files',
            field=main_app.Utility.formatChecker.ContentTypeRestrictedFileField(blank=True, null=True, upload_to='files/'),
        ),
    ]