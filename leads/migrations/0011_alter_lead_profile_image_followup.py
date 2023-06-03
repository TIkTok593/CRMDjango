# Generated by Django 4.2 on 2023-06-01 13:53

from django.db import migrations, models
import django.db.models.deletion
import leads.models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_lead_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_picture/'),
        ),
        migrations.CreateModel(
            name='Followup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=leads.models.handle_upload_follow_ups)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followups', to='leads.lead')),
            ],
        ),
    ]