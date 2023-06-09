# Generated by Django 4.1.9 on 2023-05-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emailData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.BooleanField(default=False)),
                ('unique_code', models.UUIDField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
