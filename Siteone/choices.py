from  django.db import models
from .models import *


class Distrito_Indigena(models.TextChoices):
    SI= 'S', 'SI'
    NO= 'N', 'NO'

class Tipo_Casilla(models.TextChoices):
    B= 'B', 'Básica'
    C= 'C', 'Contigua'
    ES= 'ES', 'Especial'
    E= 'E', 'Extraordinaria'

class Genero(models.TextChoices):
    M= 'M', 'Hombre'
    F= 'F', 'Mujer'
    X= 'X', 'No binario'

class yes_no_option(models.TextChoices):
    X= 'X', '-----'
    NO= 'N', 'NO'
    SI= 'S', 'SI'

class yes_no_option_full(models.TextChoices):
    X= 'X', '-----'
    NO= 'NO', 'NO'
    SI= 'SI', 'SI'

class estatus_documento(models.TextChoices):
    CA= 'CA', 'Capturado'
    FA= 'FA', 'Faltante'

class Tipo_Candidato(models.TextChoices):
    P= 'P', 'Propietario'
    S= 'S', 'Suplente'
    N= 'N', 'No aplica'

class estatus_candidato(models.TextChoices):
    DOCUMENTOS_INCOMPLETOS = 'Documentos incompletos', 'Documentos incompletos'
    DOCUMENTOS_NO_VALIDOS = 'Documentos no válidos', 'Documentos no válidos'
    NO_PRESENTAN_CREDENCIAL = 'No presentan credencial de elector', 'No presentan credencial de elector'
    NO_PRESENTAN_COMPROBANTE_DOMICILIO = 'No presentan comprobante de Domicilio', 'No presentan comprobante de Domicilio'
    DOCUMENTOS_NO_LEGIBLES = 'Documentos no legibles', 'Documentos no legibles'
    APROBADO = 'Aprobado', 'Aprobado'
    REVISADO_CON_COMENTARIOS = 'Revisado con comentarios', 'Revisado con comentarios'

class estatus_documento_Ople(models.TextChoices):
    Revisado= 'Revisado', 'Revisado'
    Aprobado= 'Aprobado', 'Aprobado'

class tipo_coalicion(models.TextChoices):
    N= 'N', '-----'
    C= 'C', 'Coalición'
    P= 'P', 'Partido'
    A= 'A', 'Candidatura común'
    I= 'I', 'Independiente'

class Tipo_Representante(models.TextChoices):
    T= 'T', 'Titular'
    S= 'S', 'Suplente'
    N= 'N', 'No aplica'

class StatusRepresentante(models.TextChoices):
    AC= 'Ac', 'Activo'
    DC= 'Dc', 'Declinado'

class TipoUsuario(models.TextChoices):
    N= 'N', '-----'
    O= 'O', 'Ople'
    P= 'P', 'Partido'
    C= 'C', 'CAE'