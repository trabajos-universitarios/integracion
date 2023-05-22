# Generated by Django 4.1.8 on 2023-05-17 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnwoListaProducto',
            fields=[
                ('nroserieanwo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('nomprodanwo', models.CharField(max_length=100)),
                ('precioanwo', models.IntegerField()),
                ('reservadoba', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'AnwoListaProducto',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('nrofac', models.IntegerField(primary_key=True, serialize=False)),
                ('fechafac', models.DateField()),
                ('descfac', models.CharField(max_length=300)),
                ('monto', models.IntegerField()),
            ],
            options={
                'db_table': 'Factura',
            },
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('rut', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tipousu', models.CharField(max_length=50)),
                ('nomusu', models.CharField(max_length=100)),
                ('apeusu', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('dirusu', models.CharField(max_length=300)),
                ('pwd', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'PerfilUsuario',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idprod', models.IntegerField(primary_key=True, serialize=False)),
                ('nomprod', models.CharField(max_length=100)),
                ('descprod', models.CharField(max_length=300)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(default='sinfoto.jpg', upload_to='images/', verbose_name='Imagen')),
            ],
            options={
                'db_table': 'Producto',
            },
        ),
        migrations.CreateModel(
            name='StockProducto',
            fields=[
                ('idstock', models.IntegerField(primary_key=True, serialize=False)),
                ('idprod', models.ForeignKey(db_column='idprod', on_delete=django.db.models.deletion.DO_NOTHING, to='core.producto')),
                ('nrofac', models.ForeignKey(blank=True, db_column='nrofac', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.factura')),
            ],
            options={
                'db_table': 'StockProducto',
            },
        ),
        migrations.CreateModel(
            name='SolicitudServicio',
            fields=[
                ('nrosol', models.IntegerField(primary_key=True, serialize=False)),
                ('tiposol', models.CharField(max_length=50)),
                ('fechavisita', models.DateField()),
                ('descsol', models.CharField(max_length=200)),
                ('estadosol', models.CharField(max_length=50)),
                ('nrofac', models.ForeignKey(db_column='nrofac', on_delete=django.db.models.deletion.DO_NOTHING, to='core.factura')),
                ('ruttec', models.ForeignKey(db_column='ruttec', on_delete=django.db.models.deletion.DO_NOTHING, to='core.perfilusuario')),
            ],
            options={
                'db_table': 'SolicitudServicio',
            },
        ),
        migrations.CreateModel(
            name='GuiaDespacho',
            fields=[
                ('nrogd', models.IntegerField(primary_key=True, serialize=False)),
                ('estadogd', models.CharField(max_length=50)),
                ('idprod', models.ForeignKey(db_column='idprod', on_delete=django.db.models.deletion.DO_NOTHING, to='core.producto')),
                ('nrofac', models.ForeignKey(db_column='nrofac', on_delete=django.db.models.deletion.DO_NOTHING, to='core.factura')),
            ],
            options={
                'db_table': 'GuiaDespacho',
            },
        ),
        migrations.AddField(
            model_name='factura',
            name='idprod',
            field=models.ForeignKey(db_column='idprod', on_delete=django.db.models.deletion.DO_NOTHING, to='core.producto'),
        ),
        migrations.AddField(
            model_name='factura',
            name='rutcli',
            field=models.ForeignKey(db_column='rutcli', on_delete=django.db.models.deletion.DO_NOTHING, to='core.perfilusuario'),
        ),
    ]
