# Generated by Django 4.2.3 on 2023-09-08 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppViajes', '0008_mensaje_thread'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='mensaje',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='usuarios',
        ),
        migrations.DeleteModel(
            name='Mensaje',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
