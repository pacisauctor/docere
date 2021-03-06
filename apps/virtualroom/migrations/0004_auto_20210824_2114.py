# Generated by Django 3.2.4 on 2021-08-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualroom', '0003_auto_20210608_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name': 'Inscripción', 'verbose_name_plural': 'Inscripciones'},
        ),
        migrations.AlterModelOptions(
            name='virtualroom',
            options={'verbose_name': 'Clase virtual', 'verbose_name_plural': 'Clases virtuales'},
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='creation_date',
            field=models.DateTimeField(editable=False, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='last_modified',
            field=models.DateTimeField(editable=False, verbose_name='Última modificación'),
        ),
        migrations.AlterField(
            model_name='virtualroom',
            name='creation_date',
            field=models.DateTimeField(editable=False, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='virtualroom',
            name='last_modified',
            field=models.DateTimeField(editable=False, verbose_name='Última modificación'),
        ),
    ]
