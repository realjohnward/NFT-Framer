# Generated by Django 3.1.7 on 2021-03-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210320_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='styles',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
