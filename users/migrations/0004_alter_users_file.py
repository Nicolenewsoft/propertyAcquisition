# Generated by Django 3.2.9 on 2021-11-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211117_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Arquivos'),
        ),
    ]
