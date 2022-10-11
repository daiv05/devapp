from django.db import models

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    dui = models.CharField(max_length=12, blank=True, null=True)
    nombre_cliente = models.CharField(max_length=1024)
    direccion = models.CharField(max_length=1024, blank=True, null=True)
    telefono = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'cliente'

class Cuenta(models.Model):
    idcuenta = models.AutoField(primary_key=True)
    codigo_cuenta = models.CharField(max_length=1024)
    tipocuenta = models.CharField(max_length=1024)
    nombre_cuenta = models.CharField(max_length=1024)

    class Meta:
        db_table = 'cuenta'

class Librodiario(models.Model):
    iddiario = models.AutoField(primary_key=True)
    idmayor = models.ForeignKey('Libromayor', models.DO_NOTHING, db_column='idmayor')
    idcuenta = models.ForeignKey(Cuenta, models.DO_NOTHING, db_column='idcuenta')
    fecha_registro = models.DateField()
    concepto = models.CharField(max_length=1024)
    cargo = models.BooleanField()
    monto = models.DecimalField(max_digits=1000, decimal_places=1000)

    class Meta:
        db_table = 'librodiario'

class Libromayor(models.Model):
    idmayor = models.AutoField(primary_key=True)
    idperiodo = models.ForeignKey('Periodo', models.DO_NOTHING, db_column='idperiodo')
    sum_debe = models.DecimalField(max_digits=1000, decimal_places=1000)
    sum_haber = models.DecimalField(max_digits=1000, decimal_places=1000)
    saldo = models.DecimalField(max_digits=1000, decimal_places=1000)
    fecha = models.DateField()

    class Meta:
        db_table = 'libromayor'

class Periodo(models.Model):
    idperiodo = models.AutoField(primary_key=True)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    activo = models.BooleanField()

    class Meta:
        db_table = 'periodo'

class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nrc = models.CharField(max_length=1024)
    razon_social = models.CharField(max_length=1024)
    contacto = models.CharField(max_length=8)
    estado = models.BooleanField()

    class Meta:
        db_table = 'proveedor'

class Usuario(models.Model):
    iduser = models.AutoField(primary_key=True)
    apellido_user = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    passwrd = models.CharField(max_length=1024)
    nombre_user = models.CharField(max_length=1024)

    class Meta:
        db_table = 'usuario'
