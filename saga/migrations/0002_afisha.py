# Generated by Django 4.2.7 on 2023-11-20 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afisha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(max_length=100, verbose_name='Название фильма Афиша')),
                ('time', models.TimeField(verbose_name='Начало фильма')),
                ('area', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
