# Generated by Django 5.0.14 on 2025-07-02 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(default='homepage', max_length=255, unique=True)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
