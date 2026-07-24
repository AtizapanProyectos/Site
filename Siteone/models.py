
from django.db import models
from .choices import Distrito_Indigena, Tipo_Casilla, Genero, yes_no_option, estatus_documento, Tipo_Candidato, estatus_candidato, estatus_documento_Ople, yes_no_option_full, tipo_coalicion, Tipo_Representante,StatusRepresentante, TipoUsuario
from django.core.validators import FileExtensionValidator
from django.db.models import UniqueConstraint

class Estados(models.Model):
    idestado = models.IntegerField(db_column='idEstado', verbose_name='Clave de la Entidad',primary_key=True, db_comment='Llave primaria de la tabla (clave única)')  # Field name made lowercase.
    nombre_edo = models.CharField(verbose_name="Nombre de la Entidad", max_length=150, blank=True, null=True, db_comment='Nombre del Estado')
    tot_habitantes = models.IntegerField(verbose_name="Total de Habitantes", blank=True, null=True, db_comment='Número total de habitantes (No se utiliza)')

    class Meta:
        managed = False
        db_table = 'estados'

    def __str__(self):
        return self.nombre_edo or self.idestado


class Actasmodif(models.Model):
    idactam = models.AutoField(db_column='IdActaM', primary_key=True, db_comment='Clave unica de Indentifiación de la acta')  # Field name made lowercase.
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', db_comment='Llave forenea de la tabla Procesos, unico inidador numerico del proceso Electoral')  # Field name made lowercase.
    idtipo_cargo = models.ForeignKey('Tipocargo', models.DO_NOTHING, db_column='idtipo_cargo', db_comment='\tLlave Foranea de la tabla tipocargo (1.- ALCALDÍA, 2.-SINDICATURA PROPIETARIA, 3.-GOBERNADOR (A), 4.-SINDICATURA SUPLENTE, 5.-REGIDURÍA PROPIETARIA, 6.-REGIDURÍA SUPLENTE, 7.-DIPUTACIÓN PROPIETARIA, 8.-DIPUTACIÓN SUPLENTE)')
    idprocesopartido = models.ForeignKey('Procesopartidos', models.DO_NOTHING, db_column='idProcesoPartido', db_comment='Llave foranea de la tabla procesospartidos, el cual indica la coalición o partido independiente en la contienda')  # Field name made lowercase.
    num_captura = models.IntegerField(db_column='Num_Captura', blank=True, null=True, db_comment='Indica la vuelta en la que se conto la acta (vuelta 1 o vuelta 2)')  # Field name made lowercase.
    votos = models.IntegerField(db_column='Votos', blank=True, null=True, db_comment='Cntidad de votos en la Contienda ')  # Field name made lowercase.
    folioc = models.ForeignKey('Casillas', models.DO_NOTHING, db_column='folioC', db_comment='Llave forenea de la tabla Casillas, identificador unico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actasmodif'

    def __str__(self):
        return self.idactam or ''  



class Arepresen(models.Model):
    idproceso = models.OneToOneField('Procesos', models.DO_NOTHING, db_column='idProceso', primary_key=True, db_comment='Llave forenea de la tabla Procesos, unico inidador numerico del proceso Electoral')  # Field name made lowercase. The composite primary key (idProceso, idtipo_doc) found, that is not supported. The first column is selected.
    idtipo_doc = models.ForeignKey('Tipodoc', models.DO_NOTHING, db_column='idtipo_doc', db_comment='Clave unica del documento y llave foranea de la tabla tipodoc')
    observa = models.CharField(max_length=60, blank=True, null=True, db_comment='Descripción del documento')
    status = models.CharField(max_length=2, blank=True, null=True, db_comment='No utilizamos la columna tiene ST por defecto')

    class Meta:
        managed = False
        db_table = 'arepresen'
        unique_together = (('idproceso', 'idtipo_doc'),)
        


class CadenaCustodiaBi(models.Model):
    descrip_proceso = models.CharField(db_column='descrip_proceso', max_length=255, db_comment='Descripción del proceso')
    cargo = models.CharField(max_length=255, db_comment='Cargo asociado')
    anio = models.IntegerField(db_column='anio', db_comment='Año del proceso')
    country = models.CharField(db_column='COUNTRY', max_length=100, db_comment='País')
    city = models.CharField(db_column='CITY', max_length=100, db_comment='Ciudad')
    nombre_mpo = models.CharField(db_column='nombre_mpo', max_length=255, db_comment='Nombre del municipio')
    casilla = models.CharField(max_length=100, db_comment='Casilla')
    id_distrito = models.CharField(db_column='idDistrito', max_length=255, db_comment='Identificador del distrito')
    id_cae = models.IntegerField(db_column='id_cae', db_comment='Identificador del CAE')
    id_paquete = models.IntegerField(db_column='idPaquete', primary_key=True, db_comment='Identificador del paquete')
    clave_ca = models.CharField(db_column='clave_ca', max_length=100, db_comment='Clave CA')
    fecha_paq = models.DateField(db_column='Fecha_paq', db_comment='Fecha de registro del paquete')
    hora_paq = models.TimeField(db_column='Hora_paq', db_comment='Hora de registro del paquete')
    latitud_ini_paq = models.DecimalField(db_column='Latitud_ini_paq', max_digits=10, decimal_places=8, db_comment='Latitud inicial del paquete')
    longitud_ini_paq = models.DecimalField(db_column='Longitud_ini_paq', max_digits=11, decimal_places=8, db_comment='Longitud inicial del paquete')
    latitud_fin_paq = models.DecimalField(db_column='Latitud_fin_paq', max_digits=10, decimal_places=8, db_comment='Latitud final del paquete')
    longitud_fin_paq = models.DecimalField(db_column='Longitud_fin_paq', max_digits=11, decimal_places=8, db_comment='Longitud final del paquete')
    estatus_paq = models.CharField(db_column='estatus_paq', max_length=100, db_comment='Estatus del paquete')
    cantidad_ruta = models.IntegerField(db_column='cantidad_ruta', db_comment='Cantidad en ruta')
    cantidad_casilla = models.IntegerField(db_column='cantidad_casilla', db_comment='Cantidad en casilla')
    cantidad_enca = models.IntegerField(db_column='cantidad_enca', db_comment='Cantidad de encargados')
    cantidad_entregadoca = models.IntegerField(db_column='cantidad_entregadoca', db_comment='Cantidad entregada al CAE')
    emergencia = models.BooleanField(db_column='Emergencia', db_comment='Indicador de emergencia')
    incidencia = models.BooleanField(db_column='Incidencia', db_comment='Indicador de incidencia')
    comentarios = models.TextField(db_column='Comentarios', db_comment='Comentarios adicionales')
    con_firma = models.CharField(max_length=5, db_comment='Indicador de paquete con firma')
    sin_muestras_alteracion = models.CharField(max_length=5, db_comment='Indicador de ausencia de muestras de alteración')
    cinta_etiqueta_seguridad = models.CharField(max_length=5, db_column='Cinta_etiqueta_seguridad', db_comment='Indicador de cinta o etiqueta de seguridad')
    sobre_prep = models.CharField(max_length=5, db_comment='Indicador de sobre PREP')
    bolsa_por_fuera = models.CharField(max_length=5, db_comment='Indicador de bolsa por fuera')

    class Meta:
        db_table = 'cadena_custodia_bi'

    def __str__(self):
        return f"{self.id_paquete}"



class Candidatos(models.Model):
    id_cand = models.AutoField(primary_key=True, db_comment='Clave unica del candidato (Auto Incrementable)')
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', db_comment='Llave forenea de la tabla Procesos, unico inidador numerico del proceso Electoral')  # Field name made lowercase.
    anio = models.IntegerField(db_comment='Año en que se registro el candidato')
    idprocesopartido = models.ForeignKey('Procesopartidos', models.DO_NOTHING, db_column='idProcesoPartido',verbose_name='Partido/Coalición', db_comment='Llave foranea de la tabla procesospartidos, nos indica la coalición a la que pertecene el candidato')  # Field name made lowercase.
    idprinc = models.ForeignKey('Principio', models.DO_NOTHING, db_column='idprinc',verbose_name='Principio', blank=True, null=True, db_comment='Llave foranea de la tabla Principios, indicador unico y con el que se ditingue el principio ( RP.-REPRESENTACIÓN PROPORCIONAL, MY.-MAYORIA RELATIVA)')
    idparidad = models.ForeignKey('Paridad', models.DO_NOTHING, db_column='idparidad', verbose_name='Acción Afirmativa', blank=True, null=True, db_comment='Indentificador unico de paredades llave foranea de la tabla paridad')
    idtipo_cargo = models.ForeignKey('Tipocargo', models.DO_NOTHING, db_column='idtipo_cargo', db_comment='Llave Foranea de la tabla tipocargo (1.- ALCALDÍA, 2.-SINDICATURA PROPIETARIA, 3.-GOBERNADOR (A), 4.-SINDICATURA SUPLENTE, 5.-REGIDURÍA PROPIETARIA, 6.-REGIDURÍA SUPLENTE, 7.-DIPUTACIÓN PROPIETARIA, 8.-DIPUTACIÓN SUPLENTE)')
    idpartido = models.ForeignKey('Partidos', models.DO_NOTHING, db_column='idPartido', db_comment='Llave foranea de la tabla partidos, indicador unico y con el que se ditingue el partido (PAN, MORENA, PT, PVEM, PRI, UDC, PRD, NV, MC)\r\n')  # Field name made lowercase.
    idestado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='idEstado', db_comment='Llave foranea de la tabla estados, indicador unico y con el que se ditingue el estado (1. Aguascalientes, 2. Baja California, 3. Baja California Sur, ..., 32. Zacatecas)', related_name='estado_residencia')
    idmunicipio = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='idMunicipio', blank=True, null=True, db_comment='Llave foranea de la tabla municipios, indicador unico y con el que se ditingue el municipio')  # Field name made lowercase.
    iddistrito = models.ForeignKey('Distritos', models.DO_NOTHING, db_column='idDistrito', blank=True, null=True, db_comment='Llave foranea de la tabla disrtitos, indicador unico y con el que se ditingue el distrito')  # Field name made lowercase.
    nombres = models.CharField(max_length=200, verbose_name='Nombre(s)', db_comment='Nombre del candidato')
    apaterno = models.CharField(max_length=200, verbose_name='Apellido Paterno',db_comment='Apellido paterno del candidato')
    amaterno = models.CharField(max_length=200, verbose_name='Apellido Materno',db_comment='Apellido materno del candidato')
    apodo = models.CharField(max_length=200,verbose_name='Sobrenombre', db_comment='Apodo del candidato')
    genero = models.CharField(max_length=2, blank=True, null=True, choices=Genero.choices, db_comment='Genero del candidato')
    idestado_nacimiento = models.ForeignKey('Estados', models.DO_NOTHING, db_column='idEstado_nacimiento', db_comment='Llave foranea de la tabla idEstado_nacimiento, indicador unico y con el que se ditingue el estado de nacimiento', related_name='estado_nacimiento')# Field name made lowercase.
    fecha_nac = models.DateField(verbose_name='Fecha de Nacimiento',db_comment='Fecha de nacimiento del candidato')
    tel = models.CharField(max_length=10, verbose_name='Número de Teléfono', db_comment='Numero telefonico del candidato')
    domicilio = models.CharField(max_length=200, verbose_name='Domicilio', db_comment='Domicilio del candidato')
    tiempo_res = models.CharField(max_length=200, verbose_name='Tiempo de Residencia', db_comment='Tiempo de residencia del candidato')
    ocupacion = models.CharField(max_length=200, verbose_name='Ocupación', db_comment='Ocupación del candidato')
    reeleccion = models.CharField(max_length=3, verbose_name='Reelección' ,blank=True, null=True, choices=yes_no_option.choices, db_comment='Reelección del candidato')
    anos_cons = models.CharField(max_length=150, verbose_name='Período',blank=True, null=True)
    grup_vul = models.CharField(max_length=3, verbose_name='¿Pertenece a un Grupo Vulnerable?',blank=True, null=True, choices=yes_no_option.choices, db_comment='Grupo vulnerable al que el candidato puede o no pertenecer a ello')
    grup_vulne = models.CharField(max_length=200, verbose_name='En su Caso Especifique', blank=True, null=True, db_comment='Grupo vulnerable al que el candidato puede o no pertenecer a ello')
    correo = models.CharField(db_column='Correo', max_length=200,verbose_name='Correo Electrónico', db_comment='Correo del candidato')  # Field name made lowercase.
    clave_elect = models.CharField(max_length=200, verbose_name='Clave Electoral',db_comment='Clave Electoral del candidato')
    cic = models.CharField(db_column='CIC', max_length=100, blank=True, null=True, db_comment='Código de Identificación de la Credencial del candidato')  # Field name made lowercase.
    ocr = models.CharField(db_column='OCR', max_length=100, blank=True, null=True, db_comment='Reconocimiento Óptico de Caracteres que se encuentra en el INE del candidato')  # Field name made lowercase.
    num_elec = models.ForeignKey('Procesoscargo', models.DO_NOTHING, db_column='num_elec', blank=True, null=True)
    num_emicion = models.CharField(max_length=200, blank=True, null=True, db_comment='Numero de emision que se encuentra en el INE candidato')
    curp = models.CharField(db_column='CURP', max_length=25, verbose_name='CURP',blank=True, null=True, db_comment='CURP del candidato')  # Field name made lowercase.
    vig_ine = models.DateField(db_column='Vig_Ine', verbose_name='Fecha de Vencimiento INE' ,blank=True, null=True, db_comment='Vigencia del INE del candidato')  # Field name made lowercase.
    aprobado = models.CharField(max_length=3, verbose_name='Aprobado',blank=True, null=True, choices=yes_no_option_full.choices,db_comment='Campo de aprobacion hacia el candidato')
    registrado = models.CharField(max_length=3,verbose_name='Capturado', blank=True, null=True,choices=yes_no_option_full.choices, db_comment='Campo que determina si el candidato ya fue registrado')
    verificado = models.CharField(max_length=3, verbose_name='Verificado',blank=True, null=True,choices=yes_no_option_full.choices ,db_comment='Campo que determina si el candidato ya fue verificado')
    centinela = models.IntegerField(db_column='Centinela', blank=True, null=True, db_comment='Se entrega de la generacion de reporte. Si centinela ==1 existe reporte, Si es ==0 no hay reporte')  # Field name made lowercase.
    fecha_de_captura = models.DateTimeField(db_column='fecha_De_captura', blank=True, null=True, db_comment='Fecha de la captura del candidato')  # Field name made lowercase.
    comentarios = models.CharField(db_column='Comentarios', max_length=1000, verbose_name='Comentarios',blank=True, null=True,choices=estatus_candidato.choices, db_comment='Comentarios del Opple hacia el candidato')  # Field name made lowercase.
    ruta = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=5, blank=True, null=True, choices=Tipo_Candidato.choices)
    num_prelacion = models.IntegerField(db_column='Num_Prelacion', verbose_name='Número de RP',blank=True, null=True, db_comment='Numero de prelacion del candidato')  # Field name made lowercase.
    id_propietario = models.ForeignKey('Candidatos', models.DO_NOTHING, db_column='id_propietario', verbose_name='Candidato Propietario',blank=True, null=True, db_comment='Identificafor unico del propietario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'candidatos'

    def __str__(self):
        return f"{self.nombres} {self.apaterno} {self.amaterno}"


class CargosEntrega(models.Model):
    id_cargo_entrega = models.CharField(db_column='ID_cargo_entrega', verbose_name="Clave del Cargo", primary_key=True, max_length=3, db_comment='Llave foranea tabla cargo_entrega (Presidente/Presidenta, 1er. Secretario/Secretaria, 2o. Secretario/Secretaria, ler. Escrutador/Escrutadora, 2o. Escrutador/Escrutadora, Supervisor/Supervisora Electoral, Capacitador/Capacitadora Asistente Electoral, Responsable de CRyT, Recepción de paquete ,OTRO)')  # Field name made lowercase.
    descripción = models.CharField(verbose_name="Descripción del Cargo",max_length=200, db_comment='Cargo de las recepeciones de casilla')


    class Meta:
        managed = False
        db_table = 'cargos_entrega'

    def __str__(self):
        return self.descripción or '' 

class Distritos(models.Model):
    idestado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='idEstado', verbose_name='Entidad Federativa', db_comment='Llave foranea e identificador única de la tabla idEstado')  
    iddistrito = models.AutoField(primary_key=True, db_column='idDistrito', verbose_name='Clave del Distrito', db_comment='llave foranea e identificador único de la tabla de distritos')  
    nombredistrito = models.CharField(max_length=50, verbose_name='Nombre del Distrito', db_comment='Nombre del Distrito')
    dirección = models.CharField(max_length=60, blank=True, null=True, verbose_name='Dirección del Distrito', db_comment='Direccion')
    distrito_indigena = models.CharField(max_length=3, blank=True, null=True, verbose_name='Distrito Indigena', db_comment='Distrito indigena')
    latitud = models.FloatField(db_column='latitud', blank=True, null=True, verbose_name='Latitud del Distrito')
    longitud = models.FloatField(db_column='longitud', blank=True, null=True,verbose_name='Longitud del Distrito')


    class Meta:
        managed = False
        db_table = 'distritos'

    def __str__(self):
        return self.nombredistrito or ''         


class CargosEntregaCasilla(models.Model):
    Id_cargo_casilla = models.AutoField(db_column='Id_cargo_casilla', primary_key=True, db_comment='Identificador único y clave foránea de la tabla ID_cargo_entrega')  # Field name made lowercase.
    id_cargo_entrega = models.ForeignKey(CargosEntrega, on_delete=models.DO_NOTHING, db_column='ID_cargo_entrega', db_comment='Identificador único y clave foránea de la tabla ID_cargo_entrega')  
    folioc = models.ForeignKey('Casillas', models.DO_NOTHING, db_column='folioC', db_comment='Folio de la persona que entrega el paquete')  
    responsable_nombre = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nombre', db_comment='Nombre de la persona que entrega el paquete')
    responsable_apaterno = models.CharField(db_column='responsable_Apaterno', max_length=200, blank=True, null=True,verbose_name='Apellido Paterno', db_comment='Apellido materno de la persona que entrega el paquete')  
    responsable_amaterno = models.CharField(db_column='responsable_Amaterno', max_length=200, blank=True, null=True,verbose_name='Apellido Materno', db_comment='Apellido paterno de la persona que entrega el paquete')  
    cargo = models.CharField(db_column='Cargo', max_length=100, blank=True, null=True, db_comment='Cargo de la persona que entrega el paquete')  



    class Meta:
        managed = False
        db_table = 'cargos_entrega_casilla'
        unique_together = (('id_cargo_entrega', 'folioc'),)

    def __str__(self):
        return f"{self.responsable_nombre} {self.responsable_apaterno} {self.responsable_amaterno}"
    


class Casillas(models.Model):
    id_casilla = models.AutoField(primary_key=True, db_column='id_casilla', db_comment='Identificador único de la casilla')  # Field name made lowercase.
    folioc = models.CharField(db_column='folioC', verbose_name="Sección", max_length=10, db_comment='Identificador único de la casilla (Sección)')  # Field name made lowercase.
    cdg_barras = models.CharField(db_column='CdgBarras', max_length=100, blank=True, null=True, db_comment='Código de barras')  # Field name made lowercase.
    cdg_qr = models.CharField(db_column='CdgQr', max_length=100, blank=True, null=True, db_comment='Código QR')  # Field name made lowercase.
    idestado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='idEstado', verbose_name="Entidad Federativa", db_comment='Identificador único del estado (llave foránea de la tabla Estados)')  # Field name made lowercase.
    idmunicipio = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='idMunicipio', verbose_name="Municipio al que pertenece la casilla", blank=True, null=True, db_comment='Identificador único del municipio (llave foránea de la tabla Municipios)')  # Field name made lowercase.
    iddistrito = models.ForeignKey('Distritos', models.DO_NOTHING, db_column='idDistrito', verbose_name="Distrito al que pertenece la casilla", related_name='distritos_casillas')  # Field name made lowercase.
    idseccion = models.CharField(db_column='idSeccion', max_length=25, verbose_name="Sección", blank=True, null=True, db_comment='Identificador único de la sección (llave foránea de la tabla Secciones)')  # Field name made lowercase.
    tipo = models.CharField(db_column='tipo', max_length=3, blank=True, null=True, choices=Tipo_Casilla.choices, verbose_name="Tipo de casilla", db_comment='B=Básica, C=Contigua, E=Extraordinaria, ES=Especial')  # Field name made lowercase.
    letra_i = models.CharField(db_column='letrai', max_length=2, blank=True, null=True, verbose_name='Letra inicial')  # Field name made lowercase.
    letra_f = models.CharField(db_column='letraf', max_length=2, blank=True, null=True, verbose_name='Letra final')  # Field name made lowercase.
    direccion = models.CharField(db_column='direccion', max_length=200, blank=True, null=True, verbose_name="Dirección", db_comment='Ubicación exacta de donde se encuentra la casilla')  # Field name made lowercase.
    capacitador = models.CharField(db_column='capacitador', max_length=50, blank=True, null=True, verbose_name='Capacitador')  # Field name made lowercase.
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', verbose_name="Elección", db_comment='Llave foránea de la tabla Procesos, único indicador numérico del proceso Electoral')  # Field name made lowercase.
    idtipo_cargo = models.ForeignKey('Tipoc', models.DO_NOTHING, db_column='idtipo_cargo', verbose_name="Cargo en el que está inmersa la casilla", blank=True, null=True, db_comment='Llave foránea de la tabla Tipocargo')  # Field name made lowercase.
    num_elec = models.ForeignKey('Procesoscargo', models.DO_NOTHING, db_column='num_elec', verbose_name="Número de Electores", blank=True, null=True, db_comment='Número de electores que se encuentran en la casilla')  # Field name made lowercase.
    id_usuario = models.ForeignKey('Inicio', models.DO_NOTHING, db_column='id_usuario', verbose_name="Usuario", blank=True, null=True, db_comment='Identificador único del usuario (llave foránea de la tabla Inicio)')  # Field name made lowercase.
    latitud_cas = models.FloatField(db_column='LATITUD_CAS', blank=True, null=True, verbose_name='Latitud de la casilla')  # Field name made lowercase.
    longitud_cas = models.FloatField(db_column='LONGITUD_CAS', blank=True, null=True, verbose_name='Longitud de la casilla')  # Field name made lowercase.
    clave_ca = models.IntegerField(db_column='clave_ca', blank=True, null=True, verbose_name='Clave de la casilla')  # Field name made lowercase.
    anio = models.IntegerField(db_column='anio', blank=True, null=True, verbose_name='Año de captura de la casilla')  # Field name made lowercase.
    idPaquete = models.IntegerField(db_column='idPaquete', blank=True, null=True, verbose_name='Paquete de la casilla')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'casillas'

    def __str__(self):
        return f"{self.folioc}- {self.direccion} "


class CatCargosOple(models.Model):
    idcargoople = models.CharField(db_column='idCargoOple', primary_key=True, max_length=3, db_comment='IdCargo del cargo del Ople')  # Field name made lowercase.
    nombre_cargo = models.CharField(max_length=200, db_comment='Nombre completo del caro del Ople')


    class Meta:
        managed = False
        db_table = 'cat_cargos_ople'

    def __str__(self):
        return self.nombre_cargo or ''         




class Consejos(models.Model):
    cdg_consejo = models.AutoField(db_column='Cdg_consejo', primary_key=True, db_comment='llave primaria de esta tabla ')  # Field name made lowercase.
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', db_comment='identificador unico de la tabla idProceso (AYUNTAMIENTO, CONGRESO, GUBERNATURA)')  # Field name made lowercase.
    tipo_consejo = models.CharField(max_length=1, db_comment='Tipo de consejo')
    descipcion = models.CharField(max_length=45, blank=True, null=True, db_comment='Nombre del consejo que se mostrara en la Aplicación')
    nombre_r = models.CharField(max_length=45, blank=True, null=True, db_comment='Nombre de del encargado')
    ap_paterno = models.CharField(max_length=45, blank=True, null=True, db_comment='Apellido paterno del encargado')
    ap_materno = models.CharField(max_length=45, blank=True, null=True, db_comment='Apellido materno del encargado')
    fecha_hora = models.DateTimeField(blank=True, null=True, db_comment='Fecha y hora de registro')
    status = models.CharField(max_length=2, blank=True, null=True)
    idtipo_cargo = models.ForeignKey('Tipocargo', models.DO_NOTHING, db_column='idtipo_cargo', db_comment='Llave Foranea de la tabla tipocargo (1.- ALCALDÍA, 2.-SINDICATURA PROPIETARIA, 3.-GOBERNADOR (A), 4.-SINDICATURA SUPLENTE, 5.-REGIDURÍA PROPIETARIA, 6.-REGIDURÍA SUPLENTE, 7.-DIPUTACIÓN PROPIETARIA, 8.-DIPUTACIÓN SUPLENTE)')



    class Meta:
        managed = False
        db_table = 'consejos'
        
    def __str__(self):
        return f"{self.descipcion}"  
    
class DocCandidatos(models.Model):
    doc_candidatos_id = models.AutoField(db_column='doc_candidatos_id', primary_key=True, db_comment='Llave primaria de esta tabla')
    idproceso = models.ForeignKey('Procesos', models.PROTECT, db_column='idProceso', db_comment='Llave foránea e identificador único del proceso (GUBERNATURA, CONGRESO, AYUNTAMIENTO)')
    idtipo_doc = models.ForeignKey('tipodoc', models.PROTECT, db_column='idtipo_doc', db_comment='Nombre y tipo de documento')

    class Meta:
        managed = False
        db_table = 'doc_candidatos'

    def __str__(self):
        return self.idtipo_doc or ''      


class DocRepresen(models.Model):
    iddoc_represen = models.AutoField(db_column='iddoc_represen', primary_key=True, db_comment='Llave primaria de esta tabla')
    cdg_repre = models.ForeignKey('Representantes', models.CASCADE, db_column='Cdg_repre', db_comment='Llave primaria de esta tabla')
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', blank=True, null=True, db_comment='Llave forenea de la tabla Procesos, unico inidador numerico del proceso Electoral')
    idtipo_doc = models.ForeignKey('Tipodoc', models.DO_NOTHING, db_column='idtipo_doc', db_comment='Tipo de Documento que se pide (Llave foranea de la tabla tipodoc)')
    archivo = models.FileField(upload_to='documentos_representantes/',validators=[FileExtensionValidator(['pdf'])], db_column='Archivo', max_length=250, blank=True, null=True, db_comment='Dirección de la computadora donde esta el archivo')
    status = models.CharField(max_length=25, blank=True, null=True, db_comment='NP= No presentadaa, CA= Capturado')

    class Meta:
        managed = False
        db_table = 'doc_represen'

    def __str__(self):
        return self.iddoc_represen or '' 

class DocumentosCandidatos(models.Model):
    id_documentos_candidatos = models.AutoField(primary_key=True, db_column='id_documentos_candidatos', db_comment='Llave primaria de esta tabla')  # Field name made lowercase.
    id_cand = models.ForeignKey(Candidatos, models.CASCADE, db_column='id_cand', db_comment='Llave foranea e identificador unico del Id del candidato')  # Cambiado a ForeignKey
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', db_comment='Id del proceso (GUBERNATURA, AYUNTAMIENTO O CONGRESO)')  # Field name made lowercase.
    idtipo_doc = models.ForeignKey('Tipodoc', models.DO_NOTHING, db_column='idtipo_doc', db_comment='Tipo de documento')
    direccion = models.FileField(upload_to='documentos_candidatos/',validators=[FileExtensionValidator(['pdf'])], null=True, db_comment='Direccion de los archivos guardados por el candidato')
    estatus = models.CharField(db_column='Estatus', max_length=100, blank=True, null=True, choices=estatus_documento.choices ,db_comment='Estatus del documento, si es existente o no')  # Field name made lowercase.
    estatus_revicion = models.CharField(db_column='Estatus_revicion', verbose_name="Estatus de Revisión",max_length=100, choices=estatus_documento_Ople.choices, blank=True, null=True, db_comment='Estatus de aprobacion para el documento subido')  # Field name made lowercase.
    comentarios = models.CharField(db_column='Comentarios', max_length=200, blank=True, null=True, db_comment='Comentarios del opple hacia el candidato dependiendo de sus documentos')  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'documentos_candidatos'
        
    def __str__(self):
        return self.id_documentos_candidatos or '' 




class Inicio(models.Model):
    id_usuario = models.AutoField(primary_key=True, db_column='id_usuario', db_comment='Llave primaria de la tabla')  # Field name made lowercase.
    correoencrip = models.CharField(db_column='CorreoEncrip', max_length=45, verbose_name='Correo Electrónico',db_comment='Correo electrónico del usuario a donde se notifica de cambios en los registros de candidaturas')  # Field name made lowercase.
    passencript = models.CharField(db_column='PassEncript', max_length=200, verbose_name='Contraseña',db_comment='Contraseña única del Usuario en el Programa')  # Field name made lowercase.
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', blank=True, null=True, db_comment='Llave foránea de la tabla Procesos, único indicador numérico del proceso Electoral')  # Field name made lowercase.
    idtipo_cargo = models.ForeignKey('Tipocargo', models.DO_NOTHING, db_column='idtipo_cargo', blank=True, null=True, db_comment='Llave foránea de la tabla tipocargo (1.- ALCALDÍA, 2.-SINDICATURA PROPIETARIA, 3.-GOBERNADOR (A), 4.-SINDICATURA SUPLENTE, 5.-REGIDURÍA PROPIETARIA, 6.-REGIDURÍA SUPLENTE, 7.-DIPUTACIÓN PROPIETARIA, 8.-DIPUTACIÓN SUPLENTE)')  # Field name made lowercase.
    anio = models.TextField(db_column='Anio', blank=True, null=True, db_comment='Año de captura del Usuario')  # Field name made lowercase. This field type is a guess.
    nombre = models.CharField(db_column='Nombre', max_length=200, db_comment='Nombre Completo del Usuario')  # Field name made lowercase.
    apaterno = models.CharField(db_column='Apaterno', max_length=200, verbose_name='Apellido Paterno',db_comment='Apellido Paterno del Usuario')  # Field name made lowercase.
    amaterno = models.CharField(db_column='Amaterno', max_length=200, verbose_name='Apellido Materno',db_comment='Apellido Materno del Usuario')  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=200, db_comment='Usuario personalizado para el usuario (con el que ingresa a la aplicación)')  # Field name made lowercase.
    tipo = models.CharField(blank=True, max_length=20,null=True,choices=TipoUsuario.choices, db_comment='No se usa esta columna')
    idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', db_comment='Llave foránea de la tabla estados, hace referencia al estado del usuario')  # Field name made lowercase.
    idpartido = models.ForeignKey('Partidos', models.DO_NOTHING,blank=True,null=True, db_column='idPartido', db_comment='Llave foránea de la tabla partidos, indica si el usuario pertenece a algún partido político')  # Field name made lowercase.
    per_partido = models.BooleanField(db_column='Per_partido', verbose_name='Permiso Partido',db_comment='1 = Acceso a las pantallas de Registro de candidaturas, configuración y Representantes para cómputos 0 = sin acceso a ellas')  # Field name made lowercase.
    per_regiscandidatura = models.BooleanField(db_column='Per_regiscandidatura', verbose_name='Permiso Registro de Candidatura',db_comment='1 = Acceso a registro de candidaturas 0 = sin acceso')  # Field name made lowercase.
    per_paquetes = models.BooleanField(db_column='Per_paquetes', verbose_name='Permiso Cadena de Custodia',db_comment='1 = Acceso a  paquetes electorales 0 = sin acceso')  # Field name made lowercase.
    per_reprecomputos = models.BooleanField(db_column='Per_reprecomputos', verbose_name='Permiso Representantes para Cómputos',db_comment='1 = Acceso a cómputos electorales 0 = sin acceso')  # Field name made lowercase.
    per_computoselectorales = models.BooleanField(db_column='Per_computoselectorales', verbose_name='Permiso Computos Electorales',db_comment='1 = Acceso a cómputos electorales 0 = sin acceso')  # Field name made lowercase.
    per_observadores = models.BooleanField(db_column='Per_Observadores', verbose_name='Permiso Observadores' ,db_comment='1 = Acceso a módulo de reportes 0 = sin acceso')  # Field name made lowercase.
    per_configuracion = models.BooleanField(db_column='Per_configuracion', verbose_name='Permiso Configuración',db_comment='1 = Acceso al módulo de Configuración 0 = sin Acceso')  # Field name made lowercase.
    per_directivo = models.BooleanField(db_column='Per_directivo', verbose_name='Permiso Directivo',db_comment='Acceso a los módulos de Configuración, Elecciones y Registro de candidaturas ')  # Field name made lowercase.
    num_telefonico = models.CharField(max_length=200, blank=True, null=True, verbose_name='Número de Teléfono',db_comment='Número telefónico del usuario para mandar notificaciones etc')
    permiso = models.CharField(max_length=100, blank=True, null=True, db_comment='Si es GLOBAL tiene accesos a todas las elecciones del estado en el que se registró ')
    activo = models.BooleanField(default=False, db_column='activo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inicio'

    def __str__(self):
        return f"{self.nombre} {self.apaterno} {self.amaterno}"

class Municipios(models.Model):
    idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', db_comment='Llave foranea de la tabla Estados nos indica el estado al que pertenece el municipio')  # Field name made lowercase.
    idmunicipio = models.AutoField(db_column='idMunicipio', primary_key=True, db_comment='Llave primaria de la tabla municipios')  # Field name made lowercase.
    nombre_mpo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre del Municipio", db_comment='Nombre del municipio')
    iddistrito = models.ForeignKey(Distritos, models.DO_NOTHING, db_column='idDistrito', db_comment='Llave foranea de la tabla distritos, indica el distrito al que pertenece')  # Field name made lowercase.
    tot_habitantes = models.IntegerField(blank=True, null=True, verbose_name="Total de habitantes")
    latitud = models.FloatField(db_column='latitud', blank=True, null=True, verbose_name='Latitud del Distrito')
    longitud = models.FloatField(db_column='longitud', blank=True, null=True,verbose_name='Longitud del Distrito')

    class Meta:
        managed = False
        db_table = 'municipios'

    def __str__(self):
        return self.nombre_mpo or '' # Solo mostrar el nombre del estado
    

class CentrosDeAcopio(models.Model):
    Idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', verbose_name='Estado: ',db_comment='Identificador unico del estado (llave foranea de la tabla Estados)')  # Field name made lowercase.
    Latitud_ca=models.FloatField(db_column='latitud_ca', blank=True, null=True, verbose_name='Latitud:')
    Longitud_ca=models.FloatField(db_column='longitud_ca', blank=True, null=True, verbose_name='Longitud:')
    Clave_ca= models.AutoField(db_column='clave_ca', primary_key=True,  verbose_name='Clave:')
    Direccion_ca=models.CharField(db_column='direccion_ca', max_length=200, blank=True, null=True, verbose_name='Dirección:')
    Anio= models.IntegerField(db_column='anio', blank=True, null=True, verbose_name='Año:')
    Nombre_ca = models.CharField(db_column='nombre_ca', max_length=200,blank=True, null=True, verbose_name='Nombre:')
    idMunicipio = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='idMunicipio', verbose_name='Municipio:')
    idDistrito = models.ForeignKey(Distritos, models.DO_NOTHING, db_column='idDistrito', verbose_name='Distrito:')

    class Meta:
        managed=False
        db_table='Centros_acopio'

    def __str__(self):
        return f"{self.Nombre_ca}"
    

class Oples(models.Model):
    idople = models.AutoField(db_column='idOple', primary_key=True, db_comment='Llave primaria de la tabla, identificador unico')  # Field name made lowercase.
    idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', db_comment='Llave foranea de la tabla Estados nos indica el estado al que pertenece el municipio')  # Field name made lowercase.    
    siglas = models.CharField(db_column='Siglas', max_length=100, db_comment='Siglas Oficiales de la Ople ')  # Field name made lowercase.
    nombre_completo = models.CharField(db_column='Nombre_completo', max_length=200, db_comment='Nombre Completo de la Ople')  # Field name made lowercase.
    logo = models.ImageField(upload_to='images/logos_Oples', db_column='Logo', max_length=200, db_comment='Ruta en donde esta almacenado el logo de la Ople en la compuradora')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'oples'

    def __str__(self):
        return self.nombre_completo or self.logo # Solo mostrar el nombre del estado

class Tipoc(models.Model):
    idtipoc = models.CharField(primary_key=True, max_length=2, db_comment='llave primaria del tipo de cargo')
    descripc = models.CharField(max_length=45, blank=True, null=True, db_comment='Descripción del proceso  como aparecera en la aplicación ')

    class Meta:
        managed = False
        db_table = 'tipoc'

    def __str__(self):
        return str(self.descripc) or ''

class Tipocargo(models.Model):
    idtipo_cargo = models.CharField(primary_key=True, max_length=3, db_comment='Llave primaria del tipo de cargo en forma numerica ')
    descrip_tcargo = models.CharField(max_length=45, blank=True, null=True, db_comment='Descripción del cargo')
    idtipoc = models.ForeignKey(Tipoc, models.DO_NOTHING, db_column='idtipoc', db_comment='Llave foranea de la tabla tipo de cargo asi es como vinculamos las elecciones con los cargos')


    class Meta:
        managed = False
        db_table = 'tipocargo'

    def __str__(self):
        return self.descrip_tcargo or ''



class Procesoscargo(models.Model):
    num_elec= models.AutoField(db_column='num_elec',primary_key=True ,blank=True, null=False, db_comment='Numero de elecciones en las que esta registrado el partido o coalición')  # Field name made lowercase.
    idproceso = models.IntegerField(db_column='idProceso', db_comment='Llave forenea de la tabla Procesos, unico inidador numerico del proceso Electoral')  # Field name made lowercase.
    idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', verbose_name='Estado al que pertenece la Elección',db_comment='Identificador unico del estado (llave foranea de la tabla Estados)')  # Field name made lowercase.
    idDistrito = models.ForeignKey(Distritos, models.DO_NOTHING, db_column='idDistrito', blank=True, null=True, db_comment='Llave foranea de la tabla distritos, nos indica el distrito al que pertenece la elección')  # Field name made lowercase.
    idMunicipio = models.ForeignKey(Municipios, models.DO_NOTHING, db_column='idMunicipio', blank=True, null=True, db_comment='Llave foranea de la tabla municipios, nos indica el municipio al que pertenece la elección')  # Field name made lowercase.
    anio = models.IntegerField(db_column='anio', null=True, blank=True)
    idtipo_cargo = models.ForeignKey(Tipocargo, models.DO_NOTHING, db_column='idtipo_cargo', blank=True, null=True, db_comment='Llave foranea de la tabla tipocargo, indica el tipo de cargo que tiene este proceso')

    class Meta:
        managed = False
        db_table = 'procesoscargo'

    def __str__(self):
        return str(self.num_elec) if self.num_elec else ''


    
class Paquetes(models.Model):
    idpaquete = models.IntegerField(db_column='idPaquete', primary_key=True, db_comment='Llave primaria de la tabla paquetes, indicador unico')  # Field name made lowercase.
    folioc = models.ForeignKey(Casillas, models.DO_NOTHING, db_column='folioC', blank=True, null=True, db_comment='Llave foranea de la tabla casillas nos indica la casilla a la que pertenece el paquete')  # Field name made lowercase.
    idtipo_cargo = models.ForeignKey('Tipocargo', models.DO_NOTHING, db_column='idtipo_cargo', blank=True, null=True, db_comment='\tLlave Foranea de la tabla tipocargo (1.- ALCALDÍA, 2.-SINDICATURA PROPIETARIA, 3.-GOBERNADOR (A), 4.-SINDICATURA SUPLENTE, 5.-REGIDURÍA PROPIETARIA, 6.-REGIDURÍA SUPLENTE, 7.-DIPUTACIÓN PROPIETARIA, 8.-DIPUTACIÓN SUPLENTE)')
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', blank=True, null=True, db_comment='Llave foranea de la tabla procesos, nos indica la elección a la que pertenece el paquete')  # Field name made lowercase.
    iddistrito = models.ForeignKey(Distritos, models.DO_NOTHING, db_column='idDistrito', blank=True, null=True, db_comment='Llave Foranea de la Tabla distrito, nos indica el distrito al que pertenece el paquete')  # Field name made lowercase.
    idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', blank=True, null=True, db_comment='Llave foranea de la tabla estados, nos indica el estado al que pertenece el paquete')  # Field name made lowercase.
    fecha_hora_entrega = models.DateTimeField(db_column='Fecha_hora_entrega', blank=True, null=True, db_comment='Fecha y hora ala que se entrego el paquete ')  # Field name made lowercase.
    lugar_entrega = models.CharField(max_length=100, blank=True, null=True, db_comment='Lugar en donde se entrego el paquete')
    con_firma = models.CharField(max_length=5, blank=True, null=True, choices=yes_no_option.choices,db_comment='Se entrgeo con firma SI o NO')
    sin_muestras_alteracion = models.CharField(max_length=5, blank=True, null=True,choices=yes_no_option.choices, db_comment='El paquete electoral se entrego con muestras de alteración SI o NO')
    cinta_etiqueta_seguridad = models.CharField(db_column='Cinta_etiqueta_seguridad', max_length=5, blank=True, null=True, choices=yes_no_option.choices, db_comment='El paquete Electoral se Entrego con la etiqueta de seguridad SI o NO')  # Field name made lowercase.
    sobre_prep = models.CharField(max_length=5, blank=True, null=True, choices=yes_no_option.choices,db_comment='El paquete se entrego con su sobrePrep SI o NO ')
    bolsa_por_fuera = models.CharField(max_length=5, blank=True, null=True, choices=yes_no_option.choices, db_comment='El paquete se entrego con su bolsa por fuera SI o NO')
    contado = models.CharField(db_column='Contado', max_length=2, blank=True, null=True, db_comment='C= Ya se contaron los votos del paquete electoral, null= no se han contado')  # Field name made lowercase.
    papeleria = models.CharField(db_column='Papeleria', max_length=2, blank=True, null=True, db_comment='Ya se ha Entregado la papelería del paquete SI o NO')  # Field name made lowercase.
    foto_entrega = models.ImageField(db_column='foto_entrega', upload_to='images/', blank=True, null=True, verbose_name="Foto del Paquete")
    foto_acta = models.ImageField(db_column='foto_acta', upload_to='images/', blank=True, null=True,verbose_name="Foto del Paquete")
    reporte = models.IntegerField(blank=True, null=True, db_comment='1= El reporte se lanzara con datos de este paquete, 0 = no se usararan los datos de ese paquete')
    num_elec=models.ForeignKey(Procesoscargo, models.DO_NOTHING, db_column='num_elec',blank=True, null=True, verbose_name='Número de Eleccion', db_comment='Número de electores que se encuentran en la casilla')  # Field name made lowercase.
    clave_ca = models.ForeignKey(CentrosDeAcopio, models.DO_NOTHING, db_column='clave_ca', blank=True, null=True, verbose_name='Se entregara en el Centro de Acopio: ', db_comment='Llave foranea de la tabla centros de acopio en donde se indica el centro de acopio al que pertenece el paquete')  # Field name made lowercase.
    anio = models.IntegerField(blank=True, null=True, db_column='anio')
    id_cargo_entrega = models.ForeignKey(CargosEntrega, models.DO_NOTHING,related_name='paquetes_entrega', db_column='ID_cargo_entrega', blank=True, null=True, db_comment='Llave Foranea de la tabla cargos_entrega nos indica el puesto o cargo que tiene la persona quien entrego el paquete')  # Field name made lowercase.
    id_usuario = models.ForeignKey(Inicio, models.DO_NOTHING, db_column='id_usuario', verbose_name='Nombre del Responsable de Recepción')
    id_cargo_recepcion = models.ForeignKey(CargosEntrega, models.DO_NOTHING, related_name='paquetes_recepcion' ,db_column='ID_cargo_recepcion', blank=True, null=True)
    nombre_recepcion = models.CharField(db_column='nombre_recepcion', max_length=100, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'paquetes'

    def __str__(self):
        return f"{self.folioc}: {self.idpaquete}"


class Paridad(models.Model):
    idparidad = models.CharField(primary_key=True,verbose_name="Clave de la Acción Afirmativa",max_length=2, db_comment='Llave primaria de la tabla paridad (Acción afirmativas)')
    descrip_paridad = models.CharField(verbose_name="Descripción Acción Afirmativa",max_length=45, blank=True, null=True, db_comment='Descripción de la paridad')

    class Meta:
        managed = False
        db_table = 'paridad'

    def __str__(self):
        return self.descrip_paridad or '' # Solo mostrar el nombre del estado
    

class Partidos(models.Model):
    idpartido = models.AutoField(db_column='idPartido', primary_key=True, db_comment='Llave primaria de la tabla partidos, indicador único')  # Field name made lowercase.
    
    partido = models.CharField(
        verbose_name="Siglas del partido",
        max_length=10,
        unique=True,  # Esta línea garantiza que cada valor sea único
        db_comment='Siglas del Partido'
    )
    desc_partido = models.CharField(
        verbose_name="Nombre completo del partido",
        max_length=200,
        unique=True,  # Esta línea garantiza que cada valor sea único
        blank=True,
        null=True,
        db_comment='Descripción completa del nombre del partido'
    )
    logo = models.ImageField(upload_to='Siteone/static/images/', verbose_name="Logo del Partido", null=False)

    def delete(self, using=None, keep_parents=False):
        self.logo.storage.delete(self.logo.name)
        super().delete()

  
    class Meta:
        managed = False
        db_table = 'partidos'

    def __str__(self):
        return self.partido or self.idpartido # Solo mostrar el nombre del estado
            



class PartidosCoaliciones(models.Model):
    idPartidosCoalicion= models.AutoField(db_column='idPartidosCoalicion', primary_key=True)
    idprocesopartido = models.ForeignKey('procesopartidos', models.PROTECT,  db_column='idProcesoPartido', db_comment='Llave primaria y foranea de la tabla procesospartido')  # Field name made lowercase. The composite primary key (idProcesoPartido, idPartido) found, that is not supported. The first column is selected.
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, blank=True, null=True, db_column='idProceso', db_comment='Llave primaria y foranea de la tabla procesos')  # Field name made lowercase.
    idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', db_comment='Llave primaria y foranea de la tabla estados')  # Field name made lowercase.
    idtipo_cargo = models.ForeignKey('Tipocargo',  models.DO_NOTHING, null=True, blank=True, db_column='idtipo_cargo', db_comment='Llave primaria y foranea de la tabla tipocargo')
    anio = models.IntegerField(db_comment='Llave primaria de esta tabla ')
    idpartido = models.ForeignKey(Partidos, models.DO_NOTHING, db_column='idPartido', db_comment='Llave primaria y foranea de la tabla partidos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'partidos_coaliciones'
        unique_together = (('idprocesopartido', 'idpartido'),)

    def __str__(self):
        return str(self.idprocesopartido) or '' # Solo mostrar el nombre del estado


class Principio(models.Model):
    idprinc = models.CharField(primary_key=True, verbose_name="Clave del Princpio" ,max_length=2, db_comment='Llave principal del principio unico indicador')
    descrip_princ = models.CharField(max_length=150, blank=True, verbose_name="Descripción del principio",null=True, db_comment='Descripción completa del principio')


    class Meta:
        managed = False
        db_table = 'principio'

    def __str__(self):
        return self.descrip_princ or '' # Solo mostrar el nombre del estado


class ProcesoCargoCasilla(models.Model):
    idtipo_cargo = models.OneToOneField('Tipocargo', models.DO_NOTHING, db_column='idtipo_cargo', primary_key=True, db_comment='\tLlave Foranea de la tabla tipocargo (1.- ALCALDÍA, 2.-SINDICATURA PROPIETARIA, 3.-GOBERNADOR (A), 4.-SINDICATURA SUPLENTE, 5.-REGIDURÍA PROPIETARIA, 6.-REGIDURÍA SUPLENTE, 7.-DIPUTACIÓN PROPIETARIA, 8.-DIPUTACIÓN SUPLENTE)')  # The composite primary key (idtipo_cargo, idProceso, folioC) found, that is not supported. The first column is selected.
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', db_comment='Llave forenea de la tabla Procesos, unico inidador numerico del proceso Electoral')  # Field name made lowercase.
    folioc = models.ForeignKey(Casillas, models.DO_NOTHING, db_column='folioC', db_comment='llave foranea de la tabla casillas nos indica que esta casilla pertenece a este proceso y cargo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proceso_cargo_casilla'
        unique_together = (('idtipo_cargo', 'idproceso', 'folioc'),)

    def __str__(self):
        return self.idtipo_cargo or '' # Solo mostrar el nombre del estado

class ProcesopartidoCandidato(models.Model):
    id_cand = models.OneToOneField(Candidatos, models.DO_NOTHING, db_column='id_cand', primary_key=True, db_comment='Llave primaria de esta tabla procesopartido_candidato')
    idprocesopartido = models.ForeignKey('Procesopartidos', models.DO_NOTHING, db_column='idProcesoPartido', db_comment='Llave Foranea de la tabla procesospartido nos indica la coalición o de partido por el que esta en contienda este cadidato')  # Field name made lowercase.
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='idProceso', db_comment='Llave foranea de la tabla procesos, nos indica la Elección que esta en contienda ')  # Field name made lowercase.
    idtipo_cargo = models.ForeignKey('Tipocargo', models.DO_NOTHING, db_column='idtipo_cargo', db_comment='\tLlave Foranea de la tabla tipocargo (1.- ALCALDÍA, 2.-SINDICATURA PROPIETARIA, 3.-GOBERNADOR (A), 4.-SINDICATURA SUPLENTE, 5.-REGIDURÍA PROPIETARIA, 6.-REGIDURÍA SUPLENTE, 7.-DIPUTACIÓN PROPIETARIA, 8.-DIPUTACIÓN SUPLENTE)')
    anio = models.IntegerField(db_comment='Año en el que se integro el candidato para la contienda ')
    nombres = models.CharField(db_column='Nombres', max_length=200, db_comment='Nombre del candidato')  # Field name made lowercase.
    appaterno = models.CharField(db_column='ApPaterno', max_length=200, db_comment='Apellido paterno del candidato')  # Field name made lowercase.
    apmaterno = models.CharField(db_column='ApMaterno', max_length=200, db_comment='Apellido materno del candidato')  # Field name made lowercase.
    sobrenombre = models.CharField(db_column='Sobrenombre', max_length=70, db_comment='Sobrenombre o Apodo del Candidato o Candidata')  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True, db_comment='No se utiliza es Estatus')  # Field name made lowercase.
    foto = models.ImageField(db_column='Foto', upload_to='Siteone/static/images/', max_length=300, blank=True, null=True, db_comment='Dirección en donde esta la foto del candidato en esta computadora')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procesopartido_candidato'

    def __str__(self):
        return f"{self.nombres}: {self.appaterno} {self.apmaterno}"        


class Procesopartidos(models.Model):
    idprocesopartido = models.AutoField(db_column='idProcesoPartido', primary_key=True, db_comment='Llave foranea de la tabla ProcesoPartido')  # Field name made lowercase.
    idproceso = models.ForeignKey('Procesos', models.DO_NOTHING, blank=True, null=True, db_column='idProceso', db_comment='Llave Foranea de la tabla procesos no indica el proceso en el que estara en contienda el partido o coalición')  # Field name made lowercase.
    idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', db_comment='Llave foranea dela tabla estados, nos indica el estado al que pertenece la coalición')  # Field name made lowercase.
    idtipo_cargo = models.ForeignKey('Tipocargo', models.DO_NOTHING, blank=True, null=True,db_column='idtipo_cargo', db_comment='Llave foranea de la tabla tipocargo nos indica el cargo al que entro en contienda esta coalición ')
    anio = models.IntegerField(db_comment='Nos indica el año en que se registro la coalición o el partido')
    tipo = models.CharField(max_length=1, blank=True, null=True, choices=tipo_coalicion.choices ,db_comment='C= coalición I= Inddependiente (Solo un partido)')
    coliacion = models.CharField(max_length=100, blank=True, null=True,verbose_name='Coalición' ,db_comment='Nombre del partido o coalición')

    class Meta:
        managed = False
        db_table = 'procesopartidos'

    def __str__(self):
        return self.coliacion or str(self.idprocesopartido) # Solo mostrar el nombre del estado

class Procesos(models.Model):
    idproceso = models.AutoField(db_column='idProceso', primary_key=True, verbose_name='Clave de la Elección',db_comment='Es la llave foranea')  # Field name made lowercase.
    anio = models.PositiveIntegerField(verbose_name='Año de la Elección',db_comment='Año del en que se usa el proceso')
    idtipoc = models.ForeignKey('Tipoc', models.DO_NOTHING, db_column='idtipoc', verbose_name='Tipo de Elección',db_comment='Llave foranea de la tabla tipocargo, indica el tipo de cargo que tiene este proceso')
    idestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='idEstado', verbose_name='Estado al que pertenece la Elección',db_comment='Identificador unico del estado (llave foranea de la tabla Estados)')  # Field name made lowercase.
    descrip = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nombre de la Elección',db_comment='Descripción del proceso')
    fecha_inicio = models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio del Proceso',db_comment='Fecha en que inicio o iniciara el proceso (Elección)')
    fecha_fin = models.DateField(blank=True, null=True, verbose_name='Fecha de Fin del Proceso',db_comment='Fecha en que termino o termino el procesoo ')
    fch_precamini = models.DateField(blank=True, null=True, verbose_name='Fecha Inicio de Pre-campaña',db_comment='Fecha en que iniciara la precampaña')
    fch_precamfin = models.DateField(blank=True, null=True, verbose_name='Fecha Fin de Pre-campaña',db_comment='Fecha en que termino o terminaran  las precampañas de esta elección')
    fch_regicandini = models.DateField(blank=True, null=True, verbose_name='Fecha Inicio de Registro de Candidatos',db_comment='Fecha de Inicio de registro de candidatos (Controla el poder registrar candidatos en la pantalla de registro de candidaturas)')
    fch_regicandfin = models.DateField(blank=True, null=True, verbose_name='Fecha Fin de Registro de Candidatos',db_comment='Fecha en que termina el proceso de registro de candidatos (Controla el poder registrar candidatos en la pantalla de registro de candidaturas)')
    fch_campanaini = models.DateField(blank=True, null=True, verbose_name='Fecha Inicio de la Campaña',db_comment='Fecha de Inicio de campaña ')
    fch_campanafin = models.DateField(blank=True, null=True, verbose_name='Fecha fin de la campaña',db_comment='Fecha fin de la campaña')
    fch_jornadaelectoral = models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio de Jornada Electoral' ,db_comment='Fecha de Inicio de Jornada Electoral')
    fch_recuento = models.DateField(blank=True, null=True, verbose_name='Fecha de Computos',db_comment='Fecha de Recuento de votos (Controla el momento en que se capturan los votos en la pantalla de computos electorales)')
    idprinc = models.ForeignKey(Principio, models.DO_NOTHING, db_column='idprinc', blank=True, null=True, verbose_name='Principio de la Elección',db_comment='Llave foranea de la tabla principio, nos indica el principio de la elección')
    idparidad = models.ForeignKey(Paridad, models.DO_NOTHING, db_column='idparidad', blank=True, null=True, verbose_name='Acción Afirmativa de la Elección',db_comment='Llave foranea de la tabla paridad, nos indica la acción afirmativa de la elección')
    total_rp = models.IntegerField(db_column='Total_RP', blank=True, null=True, verbose_name='Total de RP' ,db_comment='Limite re registro de candidatos bajo el principio de Representación proporcional y por la elección de Congreso ')  # Field name made lowercase.
    con_fotos = models.BooleanField(db_column='con_fotos', blank=True, null=True, verbose_name='Necesitan fotos los paquetes?') 
    tiempo_rastreo = models.IntegerField(db_column='tiempo_rastreo', blank=True, null=True, verbose_name='Tiempo de Rastreo',db_comment='Tiempo de rastreo del paquete de la eleccion')  # Field name made lowercase.
    ayuntamiento = models.BooleanField(db_column='Ayuntamiento', blank=True, null=True, verbose_name='Ayuntamiento')
    gubernatura = models.BooleanField(db_column='Gubernatura', blank=True, null=True, verbose_name='Gubernatura')
    congreso = models.BooleanField(db_column='Congreso', blank=True, null=True, verbose_name='Congreso')

    class Meta:
        managed = False
        db_table = 'procesos'

    def __str__(self):
        return self.descrip or self.idproceso # Solo mostrar el nombre del estado


class Representantes(models.Model):
    cdg_repre = models.AutoField(db_column='Cdg_repre', primary_key=True, db_comment='Llave primario de la tabla representantes')  # Field name made lowercase.
    idproceso = models.ForeignKey(Procesos, models.DO_NOTHING, db_column='idProceso', blank=True, null=True, db_comment='Llave forenea de la tabla Procesos, unico inidador numerico del proceso Electoral y nos indica la eleccion en la que esta registrado este representante')  # Field name made lowercase.
    idtipo_cargo = models.ForeignKey('Tipocargo', models.DO_NOTHING, db_column='idtipo_cargo', blank=True, null=True, db_comment='Llave foranea de la tabla tipocargo, nos indica el cargo al que pertenece el representante')  # Field name made lowercase.
    idprocesopartido = models.ForeignKey(Procesopartidos, models.DO_NOTHING, blank=True, null=True, db_column='idProcesoPartido', db_comment='Llave foranea de la tabla procesos partidos, nos indica a que coalición o partido pertenece el representante')  # Field name made lowercase.
    idpartido = models.ForeignKey(Partidos, models.DO_NOTHING, db_column='idPartido', db_comment='Llave foranea de la tabla partidos, nos indica al partido  que pertenece el representante ')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True, db_comment='Nombre completo del representante')  # Field name made lowercase.
    ap_paterno = models.CharField(db_column='Ap_paterno', max_length=45, blank=True, null=True,verbose_name='Apellido Paterno', db_comment='Apellido Paterno del representante')  # Field name made lowercase.
    ap_materno = models.CharField(db_column='Ap_materno', max_length=45, blank=True, null=True, verbose_name='Apellido Materno',db_comment='Apellido Materno del representante ')  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=1, blank=True, null=True,choices=Genero.choices, db_comment='Genero del representante H= Hombre M= Mujer X= no binario')  # Field name made lowercase.
    tipo_repre = models.CharField(db_column='Tipo_repre', max_length=1, blank=True, null=True,choices=Tipo_Representante.choices, db_comment='T= titular, S= Suplente')  # Field name made lowercase.
    curp = models.CharField(db_column='CURP', max_length=200, verbose_name='CURP',db_comment='Curp Completo del representante (NO SE PUEDE REPETIR UNA CURP EN NINGUN REPRESENTANTE EN LA MISMA ELECCIÓN)')  # Field name made lowercase.
    clave_elec = models.CharField(db_column='Clave_elec', max_length=200,verbose_name='Clave Electoral', db_comment='Clave electoral del representante (NO SE PUEDE REPETIR UNA CLAVE ELECTORAL EN NINGUN REPRESENTANTE EN LA MISMA ELECCIÓN)')  # Field name made lowercase.
    fecha_reg = models.DateTimeField(db_column='Fecha_reg', blank=True, null=True, db_comment='Fecha de registro del representante')  # Field name made lowercase.
    fecha_cita = models.DateField(db_column='fecha_cita', blank=True, null=True, db_comment='Fecha y hora de la cita ')  # Field name made lowercase.
    obs_repre = models.CharField(db_column='obs_repre', max_length=3,blank=True, null=True, verbose_name='Observador', db_comment='Indicador de Observador')  # Field name made lowercase.
    hora_inicio = models.TimeField(db_column='hora_inicio', blank=True, null=True, verbose_name='Hora de Inicio' ,db_comment='Hora de inicio de la cita')  # Field name made lowercase.
    hora_fin = models.TimeField(db_column='hora_fin', blank=True, null=True, verbose_name='Hora de Fin',db_comment='Hora de fin de la cita')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True, choices=StatusRepresentante.choices ,verbose_name='Estatus', db_comment='Se pone en automatico cuando registramos al representante')  # Field name made lowercase.
    asistencia = models.CharField(db_column='asistencia', max_length=5, blank=True, null=True, choices=yes_no_option.choices ,verbose_name='Asistio el Representante')
    cdg_consejo = models.ForeignKey(Consejos, models.DO_NOTHING, db_column='Cdg_consejo', blank=True, null=True, verbose_name='Consejo', db_comment='Llave foranea de la tabla consejos nos indica el consejo al que pertenece el representante')  # Field name made lowercase.
    Cdg_repretit = models.ForeignKey('Representantes', models.DO_NOTHING,db_column='Cdg_repretit', blank=True ,null=True)


    class Meta:
        managed = False
        db_table = 'representantes'

    def __str__(self):
        return f"{self.nombre}: {self.ap_paterno} {self.ap_materno}"

  
class PaquetesFase1(models.Model):

    idPaquete = models.AutoField(db_column='idPaquete', primary_key=True, db_comment='Llave primaria de esta tabla (Auto Incrementable)')  # Field name made lowercase.
    folioc = models.ForeignKey(Casillas, models.DO_NOTHING, db_column='folioC', db_comment='Llave primaria y foranea de de la tabla casillas nos indica que de que casilla es este paquete')  # Field name made lowercase.
    cantidad_boletas = models.IntegerField(db_comment='Cantidad de voletas del paquete')
    folio_inicio = models.IntegerField(db_comment='Folio de inicio del paquete electoral ')
    folio_fin = models.IntegerField(db_comment='Folio final del paquete armado')
    actas_entregadas = models.CharField(max_length=2, blank=True, null=True, choices=yes_no_option.choices, db_comment='Se entregarón las actas SI o NO')
    listasnominales_entrega = models.CharField(max_length=2, blank=True, null=True, choices=yes_no_option.choices, db_comment='Se entregaron las listas nominales SI o NO')
    fecha_entrega = models.DateField(db_comment='Fecha de entrega de paquete')
    hora_entrega = models.TimeField(db_comment='Hora de entrega del Paquete')
    idcargoople = models.ForeignKey(CatCargosOple, models.DO_NOTHING, db_column='idCargoOple', db_comment='Llave foranea de la tabla cat_cargos_ople en donde ponemos quien creo el paquete')  # Field name made lowercase.
    nombre_cargo = models.CharField(db_column='Nombre_cargo', max_length=250, verbose_name='Nombre del Responsable', db_comment='Nombre de la persona que armo el paquete')  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=2, db_comment='C= Creado F= Faltante')  # Field name made lowercase.
    reporte = models.IntegerField(blank=True, null=True, db_comment='1= reporte activo 0= reporte no activo')
    num_elec=models.ForeignKey(Procesoscargo, models.DO_NOTHING, db_column='num_elec', verbose_name='Número de Eleccion', db_comment='Número de electores que se encuentran en la casilla')  # Field name made lowercase.
    idProceso = models.ForeignKey(Procesos, models.DO_NOTHING, db_column='idProceso', verbose_name='Proceso Electoral', db_comment='Llave foranea de la tabla procesos en donde se indica el proceso al que pertenece el paquete')  # Field name made lowercase.
    clave_ca = models.ForeignKey(CentrosDeAcopio, models.DO_NOTHING, db_column='clave_ca', verbose_name='Se entregara en el Centro de Acopio: ', db_comment='Llave foranea de la tabla centros de acopio en donde se indica el centro de acopio al que pertenece el paquete')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paquetes_fase1'

    def __str__(self):
        return f"{self.folioc}: {self.idPaquete}"

  
class PaquetesFase2(models.Model):
    folioc = models.ForeignKey(Casillas, models.DO_NOTHING, db_column='folioC', db_comment='Llave foranea de la tabla casillas y primaria de paquetes')  # Field name made lowercase.
    idpaquete = models.IntegerField(db_column='idPaquete', primary_key=True, db_comment='Llave primaria de la tabla paquetes_fase2 (Auto consecutivo)')  # Field name made lowercase.
    idcargo_entrega = models.ForeignKey(CatCargosOple, models.DO_NOTHING, verbose_name="Cargo del Responsable de Entrega", db_column='idcargo_entrega', db_comment='Llave forenea de la tabla cat_cargos_ople donde podemos ver cual es el cargo ')
    nombre_cargo_entrega = models.CharField(max_length=250,verbose_name="Nombre de Quien Entrega", db_comment='Nombre de la persona que entrego el paquete')
    idcargo_recibe = models.ForeignKey(CatCargosOple, models.DO_NOTHING, verbose_name="Cargo del Responsable de Recepción", db_column='idcargo_recibe', related_name='paquetesfase2_idcargo_recibe_set', db_comment='Llave forenea de la tabla cat_cargos_ople donde podemos ver cual es el cargo (Solo puede recibir un CAE )')
    id_usuario = models.ForeignKey(Inicio, models.DO_NOTHING, db_column='id_usuario', verbose_name='Nombre del Responsable de Recepción')
    fecha_entrega = models.DateField(db_comment='Fecha de Entrega del Paquete')
    hora_entrga = models.TimeField(db_comment='Hora de Entrega del Paquete')
    estatus = models.CharField(max_length=2, db_comment='E= Entregado F=Faltante')
    reporte = models.IntegerField(blank=True, null=True, db_comment='\t1= El reporte se lanzara con datos de este paquete, 0 = no se usararan los datos de ese paquete')
    num_elec=models.ForeignKey(Procesoscargo, models.DO_NOTHING, db_column='num_elec', verbose_name='Número de Eleccion', db_comment='Número de electores que se encuentran en la casilla')  # Field name made lowercase.
    idProceso = models.ForeignKey(Procesos, models.DO_NOTHING, db_column='idProceso', verbose_name='Proceso Electoral', db_comment='Llave foranea de la tabla procesos en donde se indica el proceso al que pertenece el paquete')  # Field name made lowercase.
    clave_ca = models.ForeignKey(CentrosDeAcopio, models.DO_NOTHING, db_column='clave_ca', verbose_name='Se entregara en el Centro de Acopio: ', db_comment='Llave foranea de la tabla centros de acopio en donde se indica el centro de acopio al que pertenece el paquete')  # Field name made lowercase.
  
    class Meta:
        managed = False
        db_table = 'paquetes_fase2'

    def __str__(self):
        return f"{self.folioc}: {self.idpaquete}"
    

class PackElecFase3(models.Model):
    folioc = models.ForeignKey(Casillas, models.DO_NOTHING, db_column='folioC', db_comment='Llave primaria y foranea de de la tabla casillas nos indica que de que casilla es este paquete')  # Field name made lowercase.
    idPaquete = models.IntegerField(db_column='idPaquete', primary_key=True, db_comment='Llave primaria de esta tabla (Auto Incrementable)\t')  # Field name made lowercase.
    id_cargo_entrega = models.ForeignKey(CatCargosOple, models.DO_NOTHING,blank=True, null=True, db_column='ID_cargo_entrega', db_comment='Llave forena de la tabla cat_cargos_ople')  # Field name made lowercase.
    nombre_recibe = models.CharField(max_length=200, blank=True, null=True, verbose_name='Nombre del Responsable de Recepción:',  db_comment='Nombre completo de la persona que recivio el paquete electoral en la casilla')
    motivo = models.CharField(max_length=300, blank=True, null=True)
    estatus = models.CharField(db_column='Estatus', max_length=3, choices=yes_no_option.choices, db_comment='F = faltante E = entregado')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', db_comment='Fecha en que se entrego el paquete electoral o se rechazo ')  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', db_comment='Hora en que se rechazo el paquete electoral o se acepto ')  # Field name made lowercase.
    reporte = models.IntegerField(blank=True, null=True, db_comment='Indicador de reporte 1=  Reporte se imprimira con los datos de esta entrega 0= no hay reporte activado para este paquete ')
    id_usuario = models.ForeignKey(Inicio, models.DO_NOTHING, db_column='id_usuario', verbose_name='Nombre del Responsable de Recepción')
    id_cargo_recive= models.ForeignKey(CargosEntrega, models.DO_NOTHING, db_column='ID_cargo_recive', blank=True, null=True, verbose_name='Nombre de Quien Entrega:', db_comment='Llave foranea de la tabla cargos_entrega nos indica el puesto o cargo que tiene la persona quien recive el paquete')  # Field name made lowercase.
    num_elec=models.ForeignKey(Procesoscargo, models.DO_NOTHING, db_column='num_elec', verbose_name='Número de Eleccion', db_comment='Número de electores que se encuentran en la casilla')  # Field name made lowercase.
    idProceso = models.ForeignKey(Procesos, models.DO_NOTHING, db_column='idProceso', verbose_name='Proceso Electoral', db_comment='Llave foranea de la tabla procesos en donde se indica el proceso al que pertenece el paquete')  # Field name made lowercase.
    clave_ca = models.ForeignKey(CentrosDeAcopio, models.DO_NOTHING, db_column='clave_ca', verbose_name='Se entregara en el Centro de Acopio: ', db_comment='Llave foranea de la tabla centros de acopio en donde se indica el centro de acopio al que pertenece el paquete')  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'pack_elec_fase3'

    def __str__(self):
        return f"{self.folioc}: {self.idPaquete}"

   
class Resumenc(models.Model):
    idproceso = models.OneToOneField(Procesos, models.DO_NOTHING, db_column='idProceso', primary_key=True, db_comment='Llave forenea de la tabla Procesos, unico inidador numerico del proceso Electoral, nos indica la elección a la que pertenece')  # Field name made lowercase. The composite primary key (idProceso, idtipo_cargo) found, that is not supported. The first column is selected.
    idtipo_cargo = models.ForeignKey('Tipocargo', models.DO_NOTHING, db_column='idtipo_cargo', db_comment='\tLlave Foranea de la tabla tipocargo (1.- ALCALDÍA, 2.-SINDICATURA PROPIETARIA, 3.-GOBERNADOR (A), 4.-SINDICATURA SUPLENTE, 5.-REGIDURÍA PROPIETARIA, 6.-REGIDURÍA SUPLENTE, 7.-DIPUTACIÓN PROPIETARIA, 8.-DIPUTACIÓN SUPLENTE)')
    tot_actas = models.IntegerField(db_column='Tot_actas', blank=True, null=True, db_comment='Numero total de actas que contiene el paquete')  # Field name made lowercase.
    cotejo = models.IntegerField(blank=True, null=True, db_comment='Actas Para hacer el cotejo en computos')
    cotejadas = models.IntegerField(db_column='Cotejadas', blank=True, null=True, db_comment='Actas de cotejo que ya han sido cotejadas ')  # Field name made lowercase.
    reconteo = models.IntegerField(db_column='Reconteo', blank=True, null=True, db_comment='Actas para Reconteo debido a que tienen muestras de alteración al momento de la entrega del paquete')  # Field name made lowercase.
    recontadas = models.IntegerField(db_column='Recontadas', db_comment='Actas que ya han sido recontadas')  # Field name made lowercase.
    estatus = models.CharField(db_column='Estatus', max_length=2, db_comment='C= terminado de contar misma cantidad de actas recontadas y para recontar y actas de cotejo y para cotejar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resumenc'
        unique_together = (('idproceso', 'idtipo_cargo'),)

    def __str__(self):
        return self.idproceso or ''




class Tipodoc(models.Model):
    idtipo_doc = models.CharField(primary_key=True,verbose_name="Clave del Documento" ,max_length=5, db_comment='Llave primaria de la tabla tipodoc para indetificar el tipo de documento ')
    descrip_doc = models.CharField(verbose_name="Descripción del documento" ,max_length=45, blank=True, null=True, db_comment='Descripción del documento en cuestión')



    class Meta:
        managed = False
        db_table = 'tipodoc'

class TransladadoPaquete(models.Model):
    id_paquetetranslado = models.AutoField(primary_key=True, db_column='id_paqueteTranslado', db_comment='Llave primaria de la tabla TransladadoPaquete')
    idPaquete = models.IntegerField(db_column='idPaquete')
    folioC = models.CharField(max_length=11, db_column='folioC')
    Latitud = models.DecimalField(max_digits=16000800, decimal_places=1000)
    Longitud = models.DecimalField(max_digits=16000800, decimal_places=1000)
    Fotografia_1 = models.ImageField(upload_to='images/', verbose_name="Fotografia 1", null=False)
    Fotografia_2 = models.ImageField(upload_to='images/', verbose_name="Fotografia 2", null=False)
    Entrega = models.BooleanField()
    Llegada = models.BooleanField()
    Fecha_Hora = models.DateTimeField()
    id_usuario = models.IntegerField()
    incidencia = models.CharField(max_length=200)
    estatus = models.CharField(max_length=50)
    
    class Meta:
        managed = False
        db_table = 'transladado_paquetes'

    def __str__(self):
        return f"Paquete: {self.idPaquete} Estatus: {self.estatus}"
    


class UsuariosPantallas(models.Model):
    id_usuario_pantalla = models.AutoField(primary_key=True, db_comment='Llave primaria de la tabla usuarios_pantallas')  # Field name made lowercase.
    id_usuario = models.OneToOneField(Inicio, models.DO_NOTHING, db_column='id_usuario', db_comment='Llave foránea de la tabla inicio que nos indica qué usuario es quien va a tener estos permisos')  # Field name made lowercase.
    
    # Nuevas columnas booleanas
    revision_ople = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Revisión OPLE')
    registro_de_gubernatura = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Registro de Gubernatura')
    registro_de_ayuntamiento = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Registro de Ayuntamiento')
    diputaciones_de_mayoria = models.BooleanField( db_column='Diputaciones_de_Mayoría', blank=True, null=True, db_comment='Permiso para la pantalla de Diputaciones de Mayoría')
    diputaciones_de_rp = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Diputaciones de RP')
    armado_de_documentacion = models.BooleanField(db_column='Armado_de_Documentación',blank=True, null=True, db_comment='Permiso para la pantalla de Armado de Documentación')
    entrega_a_los_caes = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Entrega a los CAES')
    caes_entrega_a_los_presidentes = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de CAES Entrega a los Presidentes')
    entrega_de_paquetes_en_ca = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Entrega de Paquetes en CA')
    resumen_de_paquetes = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Resumen de Paquetes')
    traslado_de_paquetes = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Traslado de Paquetes')
    registro_de_representantes = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Registro de Representantes')
    representantes_ople = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Representantes Ople')
    registro_de_observadores = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Registro de Observadores')
    agregar_candidatos = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Agregar Candidatos')
    computo_de_votos = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Cómputo de Votos')
    porcentajes_de_avances = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Porcentajes de Avances')
    resumen_de_actas = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Resumen de Actas')
    votos_por_partido = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Votos por Partido')
    principios = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Principios')
    acciones_afirmativas = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Acciones Afirmativas')
    documentos = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Documentos')
    entidades_federativas = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Entidades Federativas')
    distritos = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Distritos')
    municipios = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Municipios')
    cargos_entrega = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Cargos Entrega')
    partidos = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Partidos')
    casillas = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Casillas')
    centros_de_acopio = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Centros de Acopio')
    usuarios = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Usuarios')
    tipo_eleccion = models.BooleanField(db_column='Tipo_elección',blank=True, null=True, db_comment='Permiso para la pantalla de Tipo de Elección')
    partidos_coaliciones = models.BooleanField(blank=True, null=True, db_comment='Permiso para la pantalla de Partidos/Coaliciones')
    eleccion_documentos = models.BooleanField(db_column='Elección_documentos',blank=True, null=True, db_comment='Permiso para la pantalla de Elección-documentos')

    class Meta:
        managed = False
        db_table = 'usuarios_pantallas'


class VotosPartido(models.Model):
    idvotos_partido = models.AutoField(db_column='idvotos_partido', primary_key=True)
    idprocesopartido = models.ForeignKey(Procesopartidos, models.DO_NOTHING, db_column='idProcesoPartido', db_comment='Llave Foranea de la tabla procesoPartidos nos indica a que coalición o partido pertenece estos votos')  # Field name made lowercase.
    idproceso = models.ForeignKey(Procesos, models.DO_NOTHING, db_column='idProceso', db_comment='llave forarea de la tabla procesos nos indica el proceso o elección en contienda')  # Field name made lowercase.
    idtipo_cargo = models.ForeignKey(Tipocargo, models.DO_NOTHING, db_column='idtipo_cargo', db_comment='\tLlave Foranea de la tabla tipocargo (1.- ALCALDÍA, 2.-SINDICATURA PROPIETARIA, 3.-GOBERNADOR (A), 4.-SINDICATURA SUPLENTE, 5.-REGIDURÍA PROPIETARIA, 6.-REGIDURÍA SUPLENTE, 7.-DIPUTACIÓN PROPIETARIA, 8.-DIPUTACIÓN SUPLENTE) Nos indica para que cargo son estos votos')
    idpartido = models.ForeignKey(Partidos, models.DO_NOTHING, db_column='idPartido', db_comment='llave foranea de la tabla partidos nos indica el partido en cuestión al que pertenecen los votos')  # Field name made lowercase.
    voto_partido = models.IntegerField(db_column='Voto_partido', db_comment='Cantidad de votos que recibio el partido o coalición ')  # Field name made lowercase.
    folioc = models.ForeignKey(Casillas, models.DO_NOTHING, db_column='folioC', db_comment='llave foranea de la tabla casillas que nos indica la casilla de donde se obtuvierón esos votos ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'votos_partido'

