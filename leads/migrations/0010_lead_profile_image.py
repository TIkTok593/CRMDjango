# Generated by Django 4.2 on 2023-05-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_alter_lead_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
