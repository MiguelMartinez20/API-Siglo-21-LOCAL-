# Generated by Django 3.1.1 on 2020-09-24 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='hora_ter',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
