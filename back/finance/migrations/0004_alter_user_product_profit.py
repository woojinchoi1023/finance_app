# Generated by Django 4.2.8 on 2024-05-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_user_product_profit_alter_user_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_product',
            name='profit',
            field=models.FloatField(),
        ),
    ]
