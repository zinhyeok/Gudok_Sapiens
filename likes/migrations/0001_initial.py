# Generated by Django 3.2.6 on 2021-08-08 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0002_dib_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(db_column='service_id', on_delete=django.db.models.deletion.CASCADE, related_name='services_dib', to='services.service')),
                ('users', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='service_dib', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
