# Generated by Django 3.2.4 on 2021-08-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_alter_document_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'Sección', 'verbose_name_plural': 'Secciones'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'Tema', 'verbose_name_plural': 'Temas'},
        ),
        migrations.AlterField(
            model_name='document',
            name='creation_date',
            field=models.DateTimeField(editable=False, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='document',
            name='last_modified',
            field=models.DateTimeField(editable=False, verbose_name='Última modificación'),
        ),
        migrations.AlterField(
            model_name='section',
            name='creation_date',
            field=models.DateTimeField(editable=False, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='section',
            name='last_modified',
            field=models.DateTimeField(editable=False, verbose_name='Última modificación'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='creation_date',
            field=models.DateTimeField(editable=False, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_modified',
            field=models.DateTimeField(editable=False, verbose_name='Última modificación'),
        ),
    ]