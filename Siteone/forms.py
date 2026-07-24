from django import forms
from .models import *
from django.forms import modelformset_factory
from .choices import Distrito_Indigena, yes_no_option_full
from django.conf import settings
from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404
from django.db.models import Q

from django.forms import DateInput, TimeInput

class ParidadForm(forms.ModelForm):
    class Meta:
        model = Paridad
        fields = ['idparidad', 'descrip_paridad']
 
    idparidad =forms.CharField(
        label="Clave de la Acción Afirmativa",
            error_messages={'unique': 'Este registro ya existe, favor de modificarlo'},
    )

        

class PrincForm(forms.ModelForm):
    class Meta:
        model = Principio
        fields = '__all__'

class TipodocForm(forms.ModelForm):
    class Meta:
        model = Tipodoc
        fields = '__all__'

class EstadosForm(forms.ModelForm):
    class Meta:
        model = Estados
        fields = '__all__'

class PartidosForm(forms.ModelForm):
    class Meta:
        model = Partidos
        fields = '__all__'

class CentrosdeAcopioForm(forms.ModelForm):
    idDistrito = forms.ModelChoiceField(
        queryset=Distritos.objects.all(),
        label="Distrito",
    )   

    idMunicipio = forms.ModelChoiceField(
        queryset=Municipios.objects.all(),
        label="Municipio",
    )   
    class Meta:
        model = CentrosDeAcopio
        fields = [ 'Clave_ca', 'Nombre_ca', 'Direccion_ca', 'idDistrito', 'idMunicipio','Latitud_ca', 'Longitud_ca']

class CargosEntregaForm(forms.ModelForm): 
    
    class Meta:
        model = CargosEntrega
        fields = '__all__'


class CasillasForm(forms.ModelForm):

    tipo = forms.ChoiceField(
        choices=Tipo_Casilla.choices, 
        label="Tipo de Casilla",
    )
    idmunicipio = forms.ModelChoiceField(
        queryset=Municipios.objects.all(),
        label="Municipio",
    )    
    iddistrito = forms.ModelChoiceField(
        queryset=Distritos.objects.all(),
        label="Distrito",
    )   

    class Meta:
        model = Casillas
        fields = ['iddistrito', 'idmunicipio', 'folioc', 'tipo', 'direccion', 'latitud_cas', 'longitud_cas']


    def __init__(self, *args, **kwargs):
        readonly_mode = kwargs.pop('readonly_mode', False)
        estado_id = kwargs.pop('estado_id', None)

        super(CasillasForm, self).__init__(*args, **kwargs)

        if estado_id:
            self.fields['iddistrito'].queryset = Distritos.objects.filter(idestado=estado_id)
            self.fields['idmunicipio'].queryset = Municipios.objects.filter(idestado=estado_id)

        # Si readonly_mode es True, establece todos los campos como de solo lectura
        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True


class ProcesosFrom(forms.ModelForm):

    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
        widget=forms.Select(attrs={'class': 'readonly-select'})
    )

    total_rp = forms.IntegerField(
        label=Procesos._meta.get_field('total_rp').verbose_name,
        min_value=1,
        error_messages={
            'min_value': 'El valor debe ser un entero positivo mayor que 0.'
        }
    )

    idprinc = forms.ModelChoiceField(
        queryset=Principio.objects.all(),
        label="Principio",
    )
    idparidad = forms.ModelChoiceField(
        queryset=Paridad.objects.all(),
        label="Acción Afirmativa",
    )
    ayuntamiento = forms.BooleanField(
        label=Procesos._meta.get_field('ayuntamiento').verbose_name,
        required=False
    )
    gubernatura = forms.BooleanField(
        label=Procesos._meta.get_field('gubernatura').verbose_name,
        required=False
    )
    congreso = forms.BooleanField(
        label=Procesos._meta.get_field('congreso').verbose_name,
        required=False
    )
    con_fotos = forms.BooleanField(
        label=Procesos._meta.get_field('con_fotos').verbose_name,
        required=False
    )
    anio = forms.IntegerField(
        label=Procesos._meta.get_field('anio').verbose_name,
        widget=forms.NumberInput(attrs={'readonly': 'readonly'})
    )

    class Meta:
        model = Procesos
        fields = ['idproceso', 'anio', 'ayuntamiento','gubernatura','congreso', 'idestado', 'fecha_inicio', 'fecha_fin', 'fch_precamini', 'fch_precamfin', 'fch_regicandini', 'fch_regicandfin', 'fch_campanaini', 'fch_campanafin', 'fch_jornadaelectoral', 'fch_recuento', 'tiempo_rastreo', 'total_rp', 'idprinc','idparidad','con_fotos' ]
        labels = {
            'fecha_inicio': Procesos._meta.get_field('fecha_inicio').verbose_name,
            'fecha_fin': Procesos._meta.get_field('fecha_fin').verbose_name,
            'fch_precamini': Procesos._meta.get_field('fch_precamini').verbose_name,
            'fch_precamfin': Procesos._meta.get_field('fch_precamfin').verbose_name,
            'fch_regicandini': Procesos._meta.get_field('fch_regicandini').verbose_name,
            'fch_regicandfin': Procesos._meta.get_field('fch_regicandfin').verbose_name,
            'fch_campanaini': Procesos._meta.get_field('fch_campanaini').verbose_name,
            'fch_campanafin': Procesos._meta.get_field('fch_campanafin').verbose_name,
            'fch_jornadaelectoral': Procesos._meta.get_field('fch_jornadaelectoral').verbose_name,
            'fch_recuento': Procesos._meta.get_field('fch_recuento').verbose_name,
        }


class DistritosForm(forms.ModelForm):

  idestado = forms.ModelChoiceField(
    queryset=Estados.objects.all(),
    label="Estado al que Pertenece",
    widget=forms.Select(attrs={'class': 'readonly-select'})
  )

  distrito_indigena = forms.ChoiceField(
    choices=Distrito_Indigena.choices, 
    label="Distrito Indígena",
  )



  class Meta:
     model = Distritos
     fields = ['idestado', 'iddistrito','nombredistrito' ,'dirección','distrito_indigena', 'latitud','longitud']
        
class MunicipioForm(forms.ModelForm):
    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Estado al que Pertenece",
        widget=forms.Select(attrs={'class': 'readonly-select'})
    )
        
    iddistrito = forms.ModelChoiceField(
        queryset=Distritos.objects.all(),  # Inicialmente vacío
        label="Distrito al que pertenece el Municipio",
    )
            
    class Meta:
        model = Municipios
        fields = ['idestado', 'iddistrito', 'nombre_mpo', 'tot_habitantes', 'latitud','longitud']

    def __init__(self, *args, **kwargs):
        estado_id = kwargs.pop('estado_id', None)
        super(MunicipioForm, self).__init__(*args, **kwargs)
        if estado_id:
            self.fields['iddistrito'].queryset = Distritos.objects.filter(idestado=estado_id)

class DocCandidatosFrom(forms.ModelForm):
    idproceso = forms.ModelChoiceField(
        queryset=Procesos.objects.all(),
        label="Elección",
    )
    idtipo_doc = forms.ModelChoiceField(
        queryset=Tipodoc.objects.all(),
        label="Documento",
    )

    class Meta:
        model = DocCandidatos
        fields = ['idproceso', 'idtipo_doc']  # Corregido aquí, eliminada la coma adicional


class CandidatosFormMY_Propietario(forms.ModelForm):
    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
    )
    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )
    iddistrito = forms.ModelChoiceField(
        queryset=Distritos.objects.all(),
        label="Distrito",
    )
    idparidad = forms.ModelChoiceField(
        queryset=Paridad.objects.all(),
        label="Acción Afirmativa",
    )
    genero = forms.ChoiceField(
        choices=Genero.choices,
        label="Género",
    )
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
    )
    reeleccion = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Reelección",
    )
    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
    )

    class Meta:
        model = Candidatos
        fields = ['idestado', 'iddistrito', 'idparidad' ,'nombres', 'apaterno', 'amaterno', 'genero', 'idprocesopartido', 'apodo',
                  'idestado_nacimiento', 'fecha_nac', 'curp', 'correo', 'tel', 'reeleccion', 'anos_cons', 'domicilio',
                  'tiempo_res', 'grup_vul', 'grup_vulne', 'clave_elect', 'vig_ine', 'ocupacion']

    def __init__(self, *args, **kwargs):
        readonly_mode = kwargs.pop('readonly_mode', False)
        estado_id = kwargs.pop('estado_id', None)

        super(CandidatosFormMY_Propietario, self).__init__(*args, **kwargs)

        if estado_id:
            self.fields['iddistrito'].queryset = Distritos.objects.filter(idestado=estado_id)
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        # Si readonly_mode es True, establece todos los campos como de solo lectura
        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True



class CandidatosFormMY_Propietario_Ople(forms.ModelForm):
    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
    )
    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )
    iddistrito = forms.ModelChoiceField(
        queryset=Distritos.objects.all(),
        label="Distrito",
    )
    idparidad = forms.ModelChoiceField(
        queryset=Paridad.objects.all(),
        label="Acción Afirmativa",
    )
    genero = forms.ChoiceField(
        choices=Genero.choices,
        label="Género",
    )
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
    )
    reeleccion = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Reelección",
    )
    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
    )
    aprobado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Aprobado",
        required=False,
    )

    verificado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Verificado",
        required=False,
    )


    class Meta:
        model = Candidatos
        fields = ['idestado', 'iddistrito', 'idparidad' ,'nombres', 'apaterno', 'amaterno', 'genero', 'idprocesopartido', 'apodo',
                  'idestado_nacimiento', 'fecha_nac', 'curp', 'correo', 'tel', 'reeleccion', 'anos_cons', 'domicilio',
                  'tiempo_res', 'grup_vul', 'grup_vulne', 'clave_elect', 'vig_ine', 'ocupacion', 'comentarios', 'verificado','aprobado']

    def __init__(self, *args, **kwargs):
        readonly_mode = kwargs.pop('readonly_mode', False)
        estado_id = kwargs.pop('estado_id', None)

        super(CandidatosFormMY_Propietario_Ople, self).__init__(*args, **kwargs)

        if estado_id:
            self.fields['iddistrito'].queryset = Distritos.objects.filter(idestado=estado_id)
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        # Si readonly_mode es True, establece todos los campos como de solo lectura
        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True



class CandidatosFormMY_Suplente(forms.ModelForm):

    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
    )

    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )

    iddistrito = forms.ModelChoiceField(
        queryset=Distritos.objects.all(),
        label="Distrito",
    )

    genero = forms.ChoiceField(
        choices=Genero.choices, 
        label="Género",
    )
    idparidad = forms.ModelChoiceField(
        queryset=Paridad.objects.all(),
        label="Acción Afirmativa",
    )
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
    )
    reeleccion = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Reelección",
    )
    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
    )

    id_propietario = forms.ModelChoiceField(
        queryset=Candidatos.objects.all(), 
        label="Candidato Propietario"
    )

    class Meta:
        model = Candidatos
        fields = ['id_propietario','idestado', 'iddistrito', 'idparidad', 'nombres','apaterno', 'amaterno','genero', 'idprocesopartido' , 'apodo','idestado_nacimiento', 'fecha_nac', 'reeleccion', 'anos_cons', 'grup_vul', 'grup_vulne','curp', 'correo', 'tel' ,  'domicilio', 'tiempo_res' ,  'clave_elect', 'vig_ine',  'ocupacion'] 

    def __init__(self, *args, **kwargs):
        num_elect = kwargs.pop('num_elect', None)
        estado_id = kwargs.pop('estado_id', None)
        idpartido = kwargs.pop('idpartido', None)
        principio = kwargs.pop('principio', None)
        readonly_mode = kwargs.pop('readonly_mode', False)
        super(CandidatosFormMY_Suplente, self).__init__(*args, **kwargs)
        if num_elect:
            self.fields['id_propietario'].queryset = candidatos_filtrados = Candidatos.objects.filter(
            num_elec=num_elect, tipo='P', idpartido=idpartido, idprinc=principio ).exclude(id_cand__in=Candidatos.objects.filter(id_propietario__isnull=False).values('id_propietario'))

        if estado_id:
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True



class CandidatosFormMY_Suplente_Ople(forms.ModelForm):

    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
    )

    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )

    iddistrito = forms.ModelChoiceField(
        queryset=Distritos.objects.all(),
        label="Distrito",
    )

    genero = forms.ChoiceField(
        choices=Genero.choices, 
        label="Género",
    )
    idparidad = forms.ModelChoiceField(
        queryset=Paridad.objects.all(),
        label="Acción Afirmativa",
    )
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
    )
    reeleccion = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Reelección",
    )
    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
    )

    id_propietario = forms.ModelChoiceField(
        queryset=Candidatos.objects.filter(tipo='P'), 
        label="Candidato Propietario"
    )

    aprobado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Aprobado",
        required=False,
    )

    verificado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Verificado",
        required=False,
    )
    class Meta:
        model = Candidatos
        fields = ['id_propietario','idestado', 'iddistrito', 'idparidad', 'nombres','apaterno', 'amaterno','genero', 'idprocesopartido' , 'apodo','idestado_nacimiento', 'fecha_nac', 'reeleccion', 'anos_cons', 'grup_vul', 'grup_vulne','curp', 'correo', 'tel' ,  'domicilio', 'tiempo_res' ,  'clave_elect', 'vig_ine',  'ocupacion', 'comentarios', 'verificado','aprobado'] 

    def __init__(self, *args, **kwargs):
        candidato_id = kwargs.pop('candidato_id', None)
        estado_id = kwargs.pop('estado_id', None)
        readonly_mode = kwargs.pop('readonly_mode', False)
        super(CandidatosFormMY_Suplente_Ople, self).__init__(*args, **kwargs)
        if candidato_id:
            self.fields['id_propietario'].queryset = Candidatos.objects.filter(id_cand=candidato_id.id_cand)
        if estado_id:
            self.fields['iddistrito'].queryset = Municipios.objects.filter(idestado=estado_id)
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True



class CandidatosFormAyOple(forms.ModelForm):
    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
        required=False,
    )
    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
        required=False,
    )
    idmunicipio = forms.ModelChoiceField(
        queryset=Municipios.objects.all(),
        label="Municipio",
        required=False,
    )
    genero = forms.ChoiceField(
        choices=Genero.choices,
        label="Género",
        required=False,
    )
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
        required=False,
    )
    reeleccion = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Reelección",
        required=False,
    )
    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
        required=False,
    )

    comentarios = forms.ChoiceField(
        choices=estatus_candidato.choices,
        label="Comentarios",
        required=False,
    )

    aprobado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Aprobado",
        required=False,
    )

    verificado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Verificado",
        required=False,
    )

    class Meta:
        model = Candidatos
        fields = ['idestado', 'idmunicipio', 'nombres', 'apaterno', 'amaterno', 'genero', 'idprocesopartido', 'apodo',
                  'idestado_nacimiento', 'fecha_nac', 'curp', 'correo', 'tel', 'reeleccion', 'anos_cons', 'domicilio',
                  'tiempo_res', 'grup_vul', 'grup_vulne', 'clave_elect', 'vig_ine', 'ocupacion', 'comentarios', 'verificado','aprobado']

    def __init__(self, *args, **kwargs):
        readonly_mode = kwargs.pop('readonly_mode', False)
        estado_id = kwargs.pop('estado_id', None)

        super(CandidatosFormAyOple, self).__init__(*args, **kwargs)

        if estado_id:
            self.fields['idmunicipio'].queryset = Municipios.objects.filter(idestado=estado_id)
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        # Si readonly_mode es True, establece todos los campos como de solo lectura excepto 'comentarios'
        if readonly_mode:
            for field_name, field in self.fields.items():
                if field_name != 'comentarios':
                    field.widget.attrs['readonly'] = True
                    field.widget.attrs['disabled'] = True



class ComentarDoc_Ople(forms.ModelForm):


    estatus_revicion = forms.ChoiceField(
        choices=estatus_documento_Ople.choices,
        label="Estatus de Revisión",
        required=True,
    )

    class Meta:
        model = DocumentosCandidatos
        fields = ['estatus_revicion','comentarios']


class CandidatosForm(forms.ModelForm):
    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
    )
    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )
    idmunicipio = forms.ModelChoiceField(
        queryset=Municipios.objects.all(),
        label="Municipio",
    )
    genero = forms.ChoiceField(
        choices=Genero.choices,
        label="Género",
    )
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
    )
    reeleccion = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Reelección",
    )
    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
    )

    class Meta:
        model = Candidatos
        fields = ['idestado', 'idmunicipio', 'nombres', 'apaterno', 'amaterno', 'genero', 'idprocesopartido', 'apodo',
                  'idestado_nacimiento', 'fecha_nac', 'curp', 'correo', 'tel', 'reeleccion', 'anos_cons', 'domicilio',
                  'tiempo_res', 'grup_vul', 'grup_vulne', 'clave_elect', 'vig_ine', 'ocupacion']

    def __init__(self, *args, **kwargs):
        readonly_mode = kwargs.pop('readonly_mode', False)
        estado_id = kwargs.pop('estado_id', None)

        super(CandidatosForm, self).__init__(*args, **kwargs)

        if estado_id:
            self.fields['idmunicipio'].queryset = Municipios.objects.filter(idestado=estado_id)
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        # Si readonly_mode es True, establece todos los campos como de solo lectura
        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True





class CandidatosFormGUOple(forms.ModelForm):
    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
    )
    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )

    genero = forms.ChoiceField(
        choices=Genero.choices,
        label="Género",
    )
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
    )

    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
    )


    aprobado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Aprobado",
        required=False,
    )

    verificado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Verificado",
        required=False,
    )

    class Meta:
        model = Candidatos
        fields = ['idestado', 'nombres', 'apaterno', 'amaterno', 'genero', 'idprocesopartido', 'apodo',
                  'idestado_nacimiento', 'fecha_nac', 'curp', 'correo', 'tel',  'domicilio',
                  'tiempo_res', 'grup_vul', 'grup_vulne', 'clave_elect', 'vig_ine', 'ocupacion', 'comentarios', 'verificado','aprobado']

    def __init__(self, *args, **kwargs):
        readonly_mode = kwargs.pop('readonly_mode', False)
        estado_id = kwargs.pop('estado_id', None)

        super(CandidatosFormGUOple, self).__init__(*args, **kwargs)

        if estado_id:
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        # Si readonly_mode es True, establece todos los campos como de solo lectura
        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True





class CandidatosFormGU(forms.ModelForm):
    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
    )
    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )

    genero = forms.ChoiceField(
        choices=Genero.choices,
        label="Género",
    )
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
    )

    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
    )

    class Meta:
        model = Candidatos
        fields = ['idestado', 'nombres', 'apaterno', 'amaterno', 'genero', 'idprocesopartido', 'apodo',
                  'idestado_nacimiento', 'fecha_nac', 'curp', 'correo', 'tel',  'domicilio',
                  'tiempo_res', 'grup_vul', 'grup_vulne', 'clave_elect', 'vig_ine', 'ocupacion']

    def __init__(self, *args, **kwargs):
        readonly_mode = kwargs.pop('readonly_mode', False)
        estado_id = kwargs.pop('estado_id', None)

        super(CandidatosFormGU, self).__init__(*args, **kwargs)

        if estado_id:
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        # Si readonly_mode es True, establece todos los campos como de solo lectura
        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True




class CandidatosFormSuplenteOple(forms.ModelForm):

    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
    )

    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )

    idmunicipio = forms.ModelChoiceField(
        queryset=Municipios.objects.all(),
        label="Municipio",
    )

    genero = forms.ChoiceField(
        choices=Genero.choices, 
        label="Género",
    )
    
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
    )
    reeleccion = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Reelección",
    )
    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
    )

    id_propietario = forms.ModelChoiceField(
        queryset=Candidatos.objects.filter(tipo='P'), 
        label="Candidato Propietario"
    )

    aprobado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Aprobado",
        required=False,
    )

    verificado = forms.ChoiceField(
        choices=yes_no_option_full.choices,
        label="Verificado",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        candidato_id = kwargs.pop('candidato_id', None)  # Obtener el ID del candidato si se proporciona
        estado_id = kwargs.pop('estado_id', None)
        readonly_mode = kwargs.pop('readonly_mode', False)
        super(CandidatosFormSuplenteOple, self).__init__(*args, **kwargs)

        if candidato_id:
            self.fields['id_propietario'].queryset = Candidatos.objects.filter(id_cand=candidato_id.id_cand)

        if estado_id:
            self.fields['idmunicipio'].queryset = Municipios.objects.filter(idestado=estado_id)
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True

    class Meta:
        model = Candidatos
        fields = ['id_propietario', 'idestado', 'idmunicipio', 'nombres', 'apaterno', 'amaterno', 'genero',
                  'idprocesopartido', 'apodo', 'idestado_nacimiento', 'fecha_nac', 'curp', 'correo', 'tel',
                  'reeleccion', 'anos_cons', 'domicilio', 'tiempo_res', 'grup_vul', 'grup_vulne', 'clave_elect',
                  'vig_ine', 'ocupacion', 'comentarios', 'verificado', 'aprobado']


class CandidatosFormSuplente(forms.ModelForm):

    idprocesopartido = forms.ModelChoiceField(
        queryset=Procesopartidos.objects.all(),
        label="Coalición/Partido",
    )

    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )

    idmunicipio = forms.ModelChoiceField(
        queryset=Municipios.objects.all(),
        label="Municipio",
    )

    genero = forms.ChoiceField(
        choices=Genero.choices, 
        label="Género",
    )
    
    idestado_nacimiento = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa de Nacimiento",
    )
    reeleccion = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Reelección",
    )
    grup_vul = forms.ChoiceField(
        choices=yes_no_option.choices,
        label="Grupo Vulnerable",
    )

    id_propietario = forms.ModelChoiceField(
        queryset=Candidatos.objects.filter(tipo='P').exclude(
            id_cand__in=Candidatos.objects.filter(tipo='S').values_list('id_propietario', flat=True)
        ), 
        label="Candidato Propietario"
    )

    class Meta:
        model = Candidatos
        fields = ['id_propietario','idestado', 'idmunicipio', 'nombres','apaterno', 'amaterno','genero', 'idprocesopartido' , 'apodo','idestado_nacimiento', 'fecha_nac', 'curp', 'correo', 'tel' , 'reeleccion', 'anos_cons',  'domicilio', 'tiempo_res' , 'grup_vul', 'grup_vulne', 'clave_elect', 'vig_ine',  'ocupacion'] 

    def __init__(self, *args, **kwargs):
        candidato_id = kwargs.pop('candidato_id', None)  # Obtener el ID del candidato si se proporciona
        estado_id = kwargs.pop('estado_id', None)
        readonly_mode = kwargs.pop('readonly_mode', False)
        super(CandidatosFormSuplente, self).__init__(*args, **kwargs)
        
        if candidato_id:
            self.fields['id_propietario'].queryset = Candidatos.objects.filter(id_cand=candidato_id.id_cand)

        if estado_id:
            self.fields['idmunicipio'].queryset = Municipios.objects.filter(idestado=estado_id)
            self.fields['idprocesopartido'].queryset = Procesopartidos.objects.filter(idestado=estado_id)
            self.fields['idestado'].queryset = Estados.objects.filter(idestado=estado_id)

        if readonly_mode:
            for field_name, field in self.fields.items():
                field.widget.attrs['readonly'] = True
                field.widget.attrs['disabled'] = True

class ProcesosPartidos(forms.ModelForm):


    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
        widget=forms.Select(attrs={'class': 'readonly-select'})
    )

    anio = forms.IntegerField(
        label=Procesos._meta.get_field('anio').verbose_name,
        widget=forms.NumberInput(attrs={'readonly': 'readonly'})
    )

    tipo = forms.ChoiceField(
        choices=tipo_coalicion.choices, 
        label="Tipo",
    )

    class Meta:
        model = Procesopartidos
        fields = ['idestado', 'anio','tipo', 'coliacion' ]



class Representantes_ante_computos_Titulares(forms.ModelForm):
    genero = forms.ChoiceField(
        choices=Genero.choices, 
        label="Género",
    )
    cdg_consejo = forms.ModelChoiceField(
        queryset=Consejos.objects.all(),
        label="Consejo",
    )

    fecha_cita = forms.DateField(
        label="Fecha de la cita",
        widget=DateInput(attrs={'type': 'text'}),
    )

    hora_inicio = forms.TimeField(
        label="Hora de Inicio",
        widget=TimeInput(attrs={'type': 'time'}),
    )

    hora_fin = forms.TimeField(
        label="Hora de Fin",
        widget=TimeInput(attrs={'type': 'time'}),
    )

    status = forms.ChoiceField(
        choices=StatusRepresentante.choices, 
        label="Estatus",
    )

    class Meta:
        model = Representantes
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'genero', 'curp', 'clave_elec', 'cdg_consejo', 'fecha_cita', 'hora_inicio', 'hora_fin', 'status']
    widgets = {
            'fecha_cita': DateInput(attrs={'type': 'text'}),
        }


class Representantes_Ople(forms.ModelForm):
    genero = forms.ChoiceField(
        choices=Genero.choices, 
        label="Género",
    )
    cdg_consejo = forms.ModelChoiceField(
        queryset=Consejos.objects.all(),
        label="Consejo",
    )

    hora_inicio = forms.TimeField(
        label="Hora de Inicio",
        widget=TimeInput(attrs={'type': 'time'}),
    )

    hora_fin = forms.TimeField(
        label="Hora de Fin",
        widget=TimeInput(attrs={'type': 'time'}),
    )

    status = forms.ChoiceField(
        choices=StatusRepresentante.choices, 
        label="Estatus",
    )

    asistencia = forms.ChoiceField(
        choices=yes_no_option.choices, 
        label="Asistio el Reprsentante",
    )

    class Meta:
        model = Representantes
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'genero', 'curp', 'clave_elec', 'cdg_consejo', 'fecha_cita', 'hora_inicio', 'hora_fin', 'status', 'asistencia']




class Observadoresform(forms.ModelForm):
    genero = forms.ChoiceField(
        choices=Genero.choices, 
        label="Género",
    )
    cdg_consejo = forms.ModelChoiceField(
        queryset=Consejos.objects.all(),
        label="Consejo",
    )

    fecha_cita = forms.DateField(
        label="Fecha de la cita",
        widget=DateInput(attrs={'type': 'text'}),
    )

    hora_inicio = forms.TimeField(
        label="Hora de Inicio",
        widget=TimeInput(attrs={'type': 'time'}),
    )

    hora_fin = forms.TimeField(
        label="Hora de Fin",
        widget=TimeInput(attrs={'type': 'time'}),
    )

    status = forms.ChoiceField(
        choices=StatusRepresentante.choices, 
        label="Estatus",
    )

    class Meta:
        model = Representantes
        fields = ['nombre', 'ap_paterno', 'ap_materno', 'genero', 'curp', 'clave_elec', 'cdg_consejo', 'fecha_cita', 'hora_inicio', 'hora_fin', 'status']
    widgets = {
            'fecha_cita': DateInput(attrs={'type': 'text'}),
        }

class Armado_paquetes(forms.ModelForm):

    folioc = forms.ModelChoiceField(
        queryset=Casillas.objects.all(),
        label="Pertenece a la Casilla: ",
    )
    clave_ca = forms.ModelChoiceField(
        queryset=CentrosDeAcopio.objects.all(),
        label="Se entregará en el centro de acopio: ",
    )

    idcargoople = forms.ModelChoiceField(
        queryset=CatCargosOple.objects.all(),
        label="Responsable Armado",
    )
    actas_entregadas = forms.ChoiceField(
        choices=yes_no_option.choices, 
        label="¿Se Integraron las Actas?",
    )
    listasnominales_entrega = forms.ChoiceField(
        choices=yes_no_option.choices, 
        label="¿Se Integraron las Listas Nominales?",
    )

    def __init__(self, *args, **kwargs):
        ide = kwargs.pop('ide', None)
        super(Armado_paquetes, self).__init__(*args, **kwargs)
        
        if ide:
            self.fields['folioc'].queryset = Casillas.objects.filter(
                Q(idmunicipio=ide) | Q(iddistrito=ide)
            )
            self.fields['clave_ca'].queryset = CentrosDeAcopio.objects.filter(
                Q(idMunicipio=ide) | Q(idDistrito=ide)
            )
        else:
            self.fields['folioc'].queryset = Casillas.objects.all()
            self.fields['clave_ca'].queryset = CentrosDeAcopio.objects.all()

    class Meta:
        model = PaquetesFase1
        fields = [
            'folio_inicio', 'folio_fin', 'cantidad_boletas',
            'actas_entregadas', 'listasnominales_entrega',
            'idcargoople', 'nombre_cargo', 'folioc', 'clave_ca'
        ]

class paquetes_Entrega_Cae (forms.ModelForm):
    idcargo_entrega=forms.ModelChoiceField(
        queryset=CatCargosOple.objects.all(),
        label="Cargo del Responsable de Entrega"
    )
    idcargo_recibe = forms.ModelChoiceField(
        queryset=CatCargosOple.objects.all(),
        label="Cargo del Responsable de Recepción"
    )
    id_usuario = forms.ModelChoiceField(
        queryset=Inicio.objects.all(),
        label="Nombre del Responsable de Recepción"
    )


    def __init__(self, *args, **kwargs):
        id_estado = kwargs.pop('id_estado', None)
        super(paquetes_Entrega_Cae, self).__init__(*args, **kwargs)
        
        if id_estado:
            self.fields['id_usuario'].queryset = Inicio.objects.filter(idestado=id_estado,tipo='C' )
        else:
            self.fields['id_usuario'].queryset = Inicio.objects.all()



    class Meta:
        model=PaquetesFase2
        fields=['idcargo_entrega', 'nombre_cargo_entrega', 'idcargo_recibe', 'id_usuario']


class PaquetesEntregaForm(forms.ModelForm):
    id_usuario = forms.ModelChoiceField(
        queryset=Inicio.objects.all(),
        label="Nombre del Responsable de Recepción"
    )
    class Meta:
        model = PaquetesFase2
        fields = ['idcargo_entrega', 'nombre_cargo_entrega', 'idcargo_recibe', 'id_usuario']

    def __init__(self, *args, **kwargs):
        super(PaquetesEntregaForm, self).__init__(*args, **kwargs)
        self.fields['estatus'] = forms.ChoiceField(
            choices=yes_no_option.choices,
            label="Estatus de Entrega",
        )
        self.fields['estatus'].required = False



class CAESEntregaalosPresidentes (forms.ModelForm):
    id_cargo_entrega = forms.ModelChoiceField(
        queryset=CatCargosOple.objects.all(),
        label="Cargo del Responsable de Entrega:",
    )
    estatus = forms.ChoiceField(
        choices=yes_no_option.choices, 
        label="¿Se entregó el paquete?",
    )
    id_cargo_recive = forms.ModelChoiceField(
        queryset=CargosEntrega.objects.all(),
        label="Cargo del Responsable de Recepción:",
    )
    id_usuario = forms.ModelChoiceField(
        queryset=Inicio.objects.all(),
        label="Nombre del Responsable de Recepción"
    )



    class Meta:
        model = PackElecFase3
        fields = [ 'id_cargo_entrega', 'id_usuario',  'id_cargo_recive','nombre_recibe', 'estatus']


class Responsable_de_recepcion(forms.ModelForm):

  id_cargo_entrega = forms.ModelChoiceField(
        queryset=CargosEntrega.objects.all(),
        label="Cargo",
    )

  class Meta:
    model = CargosEntregaCasilla  
    fields = ['id_cargo_entrega', 'responsable_nombre', 'responsable_apaterno', 'responsable_amaterno']


#desde aqui

class PaquetesRecoleccionCasillas(forms.ModelForm):
  id_cargo_entrega = forms.ModelChoiceField(
        queryset=CargosEntrega.objects.all(),
        label="Cargo",
    )

  class Meta:
    model = CargosEntregaCasilla  
    fields = ['id_cargo_entrega', 'responsable_nombre', 'responsable_apaterno', 'responsable_amaterno']

  def __init__(self, *args, **kwargs):

    super(PaquetesRecoleccionCasillas, self).__init__(*args, **kwargs)


    self.fields['lugar_entrega'] = forms.CharField(
    label="Lugar de Entrega", 
    widget=forms.TextInput()  # Aquí se usa el widget TextInput para campos de entrada de texto
    )


    self.fields['con_firma'] = forms.ChoiceField(
      choices=yes_no_option.choices,
      label="Con Firma",
    )

    self.fields['sin_muestras_alteracion'] = forms.ChoiceField(
      choices=yes_no_option.choices,
      label="Con Muestras de Alteración",
    )
    
    self.fields['cinta_etiqueta_seguridad'] = forms.ChoiceField(
      choices=yes_no_option.choices,
      label="Con Cinta de Seguridad", 
    )
    
    self.fields['sobre_prep'] = forms.ChoiceField(
      choices=yes_no_option.choices,
      label="Un Sobre para el PREP",
    )
    
    self.fields['bolsa_por_fuera'] = forms.ChoiceField(    
      choices=yes_no_option.choices,
      label="Una Bolsa que va por Fuera del Paquete Electoral",
    )
    self.fields['foto_entrega'] = forms.ImageField(
      label="Imagen del Paquete",
      required=False  # Puedes cambiarlo a True si la foto es obligatoria
    )
    self.fields['foto_acta'] = forms.ImageField(
      label="Imagen del Acta",
      required=False  # Puedes cambiarlo a True si la foto es obligatoria
    )



class paquetesfasee4(forms.ModelForm):

    id_cargo_entrega = forms.ModelChoiceField(
        queryset=CargosEntrega.objects.all(),
        label="Cargo",
    )

    con_firma = forms.ChoiceField(
        choices=yes_no_option.choices, 
        label="Con Firma",
    )
    sin_muestras_alteracion = forms.ChoiceField(
        choices=yes_no_option.choices, 
        label="Con Muestras de Alteración",
    )
    cinta_etiqueta_seguridad = forms.ChoiceField(
        choices=yes_no_option.choices, 
        label="Con cinta de seguridad",
    )
    sobre_prep = forms.ChoiceField(
        choices=yes_no_option.choices, 
        label="Un sobre para el PREP",
    )
    bolsa_por_fuera = forms.ChoiceField(
        choices=yes_no_option.choices, 
        label="Una bolsa que va por fuera del Paquete Electoral",
    )

    id_cargo_recepcion = forms.ModelChoiceField(
        queryset=CargosEntrega.objects.all(),
        label="Cargo",
    )

    id_usuario = forms.ModelChoiceField(
        queryset=Inicio.objects.all(),
        label="Nombre del Responsable de Recepción"
    )

    class Meta:
        model = Paquetes
        fields = ['id_cargo_entrega','id_usuario','lugar_entrega', 'con_firma', 'sin_muestras_alteracion', 'cinta_etiqueta_seguridad', 'sobre_prep', 'bolsa_por_fuera','foto_entrega', 'foto_acta', 'id_cargo_recepcion', 'nombre_recepcion']
    

class Usuarios_Agregar(forms.ModelForm):

    idproceso = forms.ModelChoiceField(
        queryset=Procesos.objects.all(),
        label="Elección",
    )
    idestado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        label="Entidad Federativa",
    )
    idtipo_cargo = forms.ModelChoiceField(
        queryset=Tipocargo.objects.all(),
        label="Cargo",
    )
    idpartido = forms.ModelChoiceField(
        queryset=Partidos.objects.all(),
        label="Partido",
        required=False,
    )
    tipo = forms.ChoiceField(
        choices=TipoUsuario.choices, 
        label="Tipo de Usuario",
    )


    class Meta:
        model = Inicio
        fields = ['idestado','idproceso','idtipo_cargo', 'correoencrip','passencript','num_telefonico', 'nombre', 'apaterno','amaterno', 'usuario', 'tipo','idpartido','per_partido',
                  'per_regiscandidatura','per_paquetes','per_reprecomputos', 'per_computoselectorales','per_observadores','per_configuracion','per_directivo']



class procesos_partidos(forms.ModelForm):
        idpartido = forms.ModelChoiceField(
        queryset=Partidos.objects.all(),
        label="Partido",
        required=False,
    )
        
class Meta:
        model = PartidosCoaliciones
        fields = ['idpartido']    