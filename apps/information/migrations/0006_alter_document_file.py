# Generated by Django 3.2.7 on 2021-09-14 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0005_alter_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='topics/%Y/%m/%d'),
        ),
    ]
