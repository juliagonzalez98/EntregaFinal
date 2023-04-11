# Generated by Django 4.1.7 on 2023-04-11 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_articulos_autor_articulos_cuerpo_articulos_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
