# Generated by Django 4.1.7 on 2023-03-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('gender', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('re_password', models.CharField(max_length=100)),
            ],
        ),
    ]
