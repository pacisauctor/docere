# Generated by Django 3.2.4 on 2021-06-09 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_auto_20210609_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='information.topic', verbose_name='archivos'),
        ),
    ]
