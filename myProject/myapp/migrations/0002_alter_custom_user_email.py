# Generated by Django 5.0 on 2023-12-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
