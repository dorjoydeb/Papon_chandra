# Generated by Django 3.2.6 on 2021-11-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_remove_email_info_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='email_info',
            name='Phone',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
