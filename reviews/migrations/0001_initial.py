# Generated by Django 3.2.6 on 2021-08-06 05:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='리뷰사진')),
                ('title', models.CharField(max_length=50, verbose_name='리뷰제목')),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(15)], verbose_name='내용')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='별점')),
                ('period', models.PositiveSmallIntegerField(verbose_name='사용기간')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='likes.like', verbose_name='좋아요')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='서비스')),
            ],
        ),
    ]