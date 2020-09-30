# Generated by Django 3.1.1 on 2020-09-30 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_producto_embalaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='embalaje',
            field=models.CharField(choices=[('GRANEL', 'GRANEL'), ('ENVASADO', 'ENVASADO')], default='GRANEL', max_length=11),
        ),
    ]