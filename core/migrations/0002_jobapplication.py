# Generated by Django 5.0.1 on 2024-02-16 11:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('interview_data', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('APPLIED', 'Applied'), ('SCREENING', 'Screening'), ('SHORT_LISTED', 'Short_Listed'), ('REJECTED', 'Rejected'), ('SELECTED', 'Selected')], max_length=20)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='core.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_application', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
