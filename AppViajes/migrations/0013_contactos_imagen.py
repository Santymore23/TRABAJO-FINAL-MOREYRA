# Generated by Django 4.2.3 on 2023-09-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppViajes', '0012_alter_avatar_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactos',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='contactos_images/'),
        ),
    ]