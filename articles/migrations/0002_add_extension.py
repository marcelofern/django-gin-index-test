# Generated by Django 5.0.4 on 2024-05-02 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("CREATE EXTENSION IF NOT EXISTS pg_trgm;")
    ]
