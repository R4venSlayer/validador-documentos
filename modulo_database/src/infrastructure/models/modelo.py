# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Informacionpersona(models.Model):
    id_persona = models.CharField(max_length=36)
    primer_nombre = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    segundo_nombre = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    primer_apellido = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    segundo_apellido = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    numero_documento = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tipo_documento = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    estado_civil = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    direccion_residencia = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    zona = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    barrio = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    localidad = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    departamento_residencia = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    municipio_residencia = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    estrato = models.IntegerField(blank=True, null=True)
    correo_electronico = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    numero_celular = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    telefono_fijo = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    departamento_laboral = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    municipio_laboral = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    secretaria = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    institucion_educativa = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    discapacidad = models.CharField(max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tipo_discapacidad = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    grupo_etnico = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    poblacion_lgbtiq = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tipo_afiliado = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'InformacionPersona'


class Municipio(models.Model):
    id = models.CharField(primary_key=True, max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')
    region_id = models.IntegerField()
    descripcion_mun = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    descripcion_dep = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'municipio'

class Afiliados(models.Model):
    id_hospital = models.IntegerField()
    primer_nombre = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    segundo_nombre = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    primer_apellido = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    segundo_apellido = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tipo_documento = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    numero_documento = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sexo = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    edad_cumplida = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    parentesco = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tipo_afiliado = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    fecha_afiliacion = models.DateField(blank=True, null=True)
    fecha_retiro = models.DateField(blank=True, null=True)
    tipo_documento_cotizante = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tipo_cotizante = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    numero_documento_cotizante = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    estado_afiliacion = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    codigo_dane_depto_atencion = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    departamento_atencion = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    codigo_dane_municipio_atencion = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    municipio_atencion = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ips_primaria = models.CharField(db_column='IPS_Primaria', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    celular_principal = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    celular_alterno = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    correo_principal = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    direccion_residencia_cargue = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    zona = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    region = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nit = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nombre_prestador = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    discapacidad = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    grado_discapacidad = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    afiliado_id = models.IntegerField(blank=True, null=True)
    entidad_id = models.IntegerField(blank=True, null=True)
    codigo_habilitacion_sede_prim = models.CharField(max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    municipio_residencia = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    departamento_residencia = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Afiliados'