# Generated by Django 4.1.7 on 2023-05-31 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, max_length=100000000000000000, null=True),
        ),
    ]