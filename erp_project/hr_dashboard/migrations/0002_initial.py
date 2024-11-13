# Generated by Django 5.1.3 on 2024-11-13 08:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hr_dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salaries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payrolladjustment',
            name='salary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adjustments', to='hr_dashboard.salary'),
        ),
    ]
