# Generated by Django 3.2.4 on 2021-06-09 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtualroom', '0003_auto_20210608_2002'),
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='virtualroom',
        ),
        migrations.AddField(
            model_name='section',
            name='virtualroom',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='virtualroom.virtualroom', verbose_name='Clase virtual'),
            preserve_default=False,
        ),
    ]
