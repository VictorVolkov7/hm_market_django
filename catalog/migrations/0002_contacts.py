# Generated by Django 4.2.5 on 2023-09-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, verbose_name='телефон')),
                ('telegram', models.CharField(max_length=50, verbose_name='телеграмм')),
                ('vk', models.CharField(max_length=50, verbose_name='ВКонтакте')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
            },
        ),
    ]
