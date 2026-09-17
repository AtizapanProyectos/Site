from django.db import models


class ServiciosManager(models.Manager):
    """Manager que apunta automáticamente a la base de datos 'servicios'."""
    def get_queryset(self):
        return super().get_queryset().using('servicios')


class CrmContacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    organizacion = models.CharField(max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, default='cliente', blank=True, null=True)
    usuario = models.CharField(max_length=100, default='lidia')
    activo = models.BooleanField(default=True)
    notas = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    objects = ServiciosManager()

    class Meta:
        managed = False
        db_table = 'crm_contactos'
        verbose_name = 'Contacto CRM'
        verbose_name_plural = 'Contactos CRM'

    @property
    def nombre_completo(self):
        if self.apellidos:
            return f"{self.nombre} {self.apellidos}".strip()
        return self.nombre.strip()

    def __str__(self):
        org = f" [{self.organizacion}]" if self.organizacion else ""
        return f"{self.nombre_completo}{org} ({self.telefono}) [{self.usuario}]"


class CrmColaWhatsapp(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('error', 'Error'),
    ]

    id = models.AutoField(primary_key=True)
    telefono = models.CharField(max_length=20)
    nombre_contacto = models.CharField(max_length=120, blank=True, null=True)
    mensaje = models.TextField()
    usuario = models.CharField(max_length=100, default='lidia')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    fecha_programada = models.DateField()
    intentos = models.IntegerField(default=0)
    error_detalle = models.TextField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    enviado_en = models.DateTimeField(blank=True, null=True)

    objects = ServiciosManager()

    class Meta:
        managed = False
        db_table = 'crm_cola_whatsapp'
        verbose_name = 'Mensaje en Cola WhatsApp'
        verbose_name_plural = 'Cola de Mensajes WhatsApp'

    def __str__(self):
        return f"[{self.estado}] {self.nombre_contacto or self.telefono} - {self.fecha_programada} ({self.usuario})"
