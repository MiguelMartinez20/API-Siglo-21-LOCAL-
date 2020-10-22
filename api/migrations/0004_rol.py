# Generated by Django 3.1.1 on 2020-10-22 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_notificacion_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('ADMINISTRADOR', 'ADMINISTRADOR'), ('COCINA', 'COCINA'), ('BODEGA', 'BODEGA'), ('FINANZAS', 'FINANZAS'), ('GARZON', 'GARZON'), ('CLIENTE', 'CLIENTE')], default='CLIENTE', max_length=14)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
