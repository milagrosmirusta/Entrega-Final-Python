# Generated by Django 4.2.6 on 2023-11-17 04:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplication', '0002_rename_dir_mail_cliente_direccion_mail_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='producto',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='rubro',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='subrubro',
        ),
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=ckeditor.fields.RichTextField(default='Sin descripción'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='productos'),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
