# Generated by Django 4.2.5 on 2023-10-23 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_is_published', 'Can publish posts'), ('set_title', 'Can change title'), ('set_category', 'Can change category')], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
    ]
