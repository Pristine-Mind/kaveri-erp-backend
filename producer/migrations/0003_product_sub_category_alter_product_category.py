# Generated by Django 4.2.18 on 2025-01-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0002_rename_producer_supplier_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(blank=True, choices=[('SB', 'Strong Beer'), ('PB', 'Premium Beer'), ('SE', 'Special Edition')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BV', 'Beverage')], default='BV', max_length=2),
        ),
    ]
