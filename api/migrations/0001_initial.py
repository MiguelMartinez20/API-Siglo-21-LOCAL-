# Generated by Django 3.1.1 on 2020-10-15 01:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('run', models.CharField(max_length=8)),
                ('dv', models.CharField(default='0', max_length=1)),
                ('nombre', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('capacidad', models.IntegerField(blank=True)),
                ('disponibilidad', models.CharField(choices=[('OCUPADA', 'OCUPADA'), ('RESERVADA', 'RESERVADA'), ('DISPONIBLE', 'DISPONIBLE')], default='DISPONIBLE', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('ingreso', models.IntegerField(default=0)),
                ('egreso', models.IntegerField(default=0)),
                ('fecha', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('metodo', models.CharField(choices=[('EFECTIVO', 'EFECTIVO'), ('CREDITO/DEBITO', 'CREDITO/DEBITO')], default='EFECTIVO', max_length=14)),
                ('detalle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('costo', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('embalaje', models.CharField(choices=[('GRANEL', 'GRANEL'), ('ENVASADO', 'ENVASADO')], default='GRANEL', max_length=11)),
                ('detalle', models.CharField(blank=True, max_length=300)),
                ('movimiento', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.movimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('observacion', models.CharField(blank=True, max_length=255)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
                ('mesa_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mesa')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('t_preparacion', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('grupo', models.CharField(choices=[('ENTRADA', 'ENTRADA'), ('PLATO_FONDO', 'PLATO_FONDO'), ('APERITIVO', 'APERITIVO'), ('AGREGADO', 'AGREGADO'), ('BEBESTIBLE', 'BEBESTIBLE'), ('POSTRE', 'POSTRE')], default='ENTRADA', max_length=20)),
                ('sub_grupo', models.CharField(choices=[('SOPAS', 'SOPAS'), ('CREMAS', 'CREMAS'), ('CARNES_ROJAS', 'CARNES_ROJAS'), ('CARNES_BLANCAS', 'CARNES_BLANCAS'), ('PESCADOS', 'PESCADOS'), ('MARISCOS', 'MARISCOS'), ('CALDOS', 'CALDOS'), ('LEGUMBRES', 'LEGUMBRES'), ('PASTELES', 'PASTELES'), ('EMBUTIDOS', 'EMBUTIDOS'), ('EMPANADAS', 'EMPANADAS'), ('VINOS', 'VINOS'), ('BEBIDAS', 'BEBIDAS'), ('JUGOS', 'JUGOS'), ('BAJATIVO', 'BAJATIVO'), ('HELADOS', 'HELADOS'), ('TORTAS', 'TORTAS'), ('KUCHENS', 'KUCHENS'), ('OTRO', 'OTRO')], max_length=20)),
                ('productos', models.ManyToManyField(to='api.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('numero', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('ENTREGADA', 'ENTREGADA'), ('LISTA', 'LISTA'), ('PREPARACION', 'PREPARACION')], default='PREPARACION', max_length=11)),
                ('hora_ini', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('hora_ter', models.DateTimeField(blank=True, null=True)),
                ('detalle', models.CharField(blank=True, max_length=255)),
                ('total', models.IntegerField(blank=True)),
                ('minutos', models.IntegerField(blank=True, default=5)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mesa')),
                ('movimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.movimiento')),
                ('recetas', models.ManyToManyField(to='api.Receta')),
            ],
        ),
    ]
