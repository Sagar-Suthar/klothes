# Generated by Django 4.0.3 on 2022-05-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_product_shirts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirts',
            name='image',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
