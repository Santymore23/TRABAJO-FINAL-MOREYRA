# Generated by Django 4.2.3 on 2023-09-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppViajes', '0013_contactos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='destino_images/'),
        ),
    ]