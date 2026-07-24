from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('',views.Pagina, name='Pagina'),
    path('Login',views.Login, name='login'),
    path('Inicio',views.inicio, name='inicio'),
    path('verification', views.verification, name='verification'),

    path('nosotros',views.nosotros, name='nosotros'),
    path('paridad',views.paridades, name='paridad'),
    path('principio',views.principio, name='principio'),
    path('principio/agregar',views.principios_agregar, name='principios_agregar'),
    path('principio/eliminar<str:id>',views.principio_eliminar, name='principio_eliminar'),
    path('paridad/agregar',views.paridades_agregar, name='paridad_agregar'),
    path('principio/editar/<str:id>',views.principios_editar, name='principio_editar'),
    path('paridad/eliminar/<str:id>',views.paridades_eliminar, name='paridades_eliminar'),
    path('paridad/editar/<str:id>', views.paridades_editar, name='paridades_editar'),
    path('estados',views.estados, name='estados'),
    path('partidos',views.partidos, name='partidos'),

    path('documentos',views.documentos, name='documentos'),
    path('documentos/agregar',views.documentos_agregar, name='doc_agregar'),
    path('documentos/eliminar/<str:id>',views.documentos_eliminar, name='doc_eliminar'),
    path('documentos/editar/<str:id>', views.documentos_editar, name='doc_editar'),

     path('entidadesfederativas',views.estados, name='estados'),
    path('entidadesfederativas/agregar',views.estados_agregar, name='estados_agregar'),
    path('entidadesfederativas/eliminar/<int:id>',views.estados_eliminar, name='estados_eliminar'),
    path('entidadesfederativas/editar/<int:id>', views.estados_editar, name='estados_editar'),


     path('Partidospoliticos',views.partidos, name='partidos'),
    path('Partidospoliticos/agregar',views.partidos_agregar, name='partidos_agregar'),
    path('Partidospoliticos/eliminar/<int:id>',views.partidos_eliminar, name='partidos_eliminar'),
    path('Partidospoliticos/editar/<int:id>', views.partidos_editar, name='partidos_editar'),

    path('cargosdeentrega',views.cargosentrega, name='cargosentrega'),
    path('cargosdeentrega/agregar',views.cargosentrega_agregar, name='cargosentrega_agregar'),
    path('cargosentrega/eliminar/<str:id>',views.cargosentrega_eliminar, name='cargosentrega_eliminar'),
    path('cargosentrega/editar/<str:id>', views.cargosentrega_editar, name='cargosentrega_editar'),

    path('casillas',views.casillas, name='casillas'),
    path('casillasget/<int:iddistrito>/<str:nombreeleccion>/', views.casilla_consulta, name='casillasget'),
    path('casillas/agregar/<str:eleccion>/<int:iddistrito>/<int:anio>/<int:idestado>', views.casillas_agregar, name='casillas_agregar'),
    path('casillas/eliminar/<str:id>',views.casillas_eliminar, name='casillas_eliminar'),
    path('casillas/editar/<str:id>/<str:eleccion>/<int:iddistrito>/<int:anio>', views.casillas_editar, name='casillas_editar'),



    path('centros/acopio',views.centros_acopio, name='centros_ca'),
    path('centros/acopio/get/<int:idestado>/', views.centros_acopio_consulta, name='centros_acopio_get'),
    path('centros/acopio/agregar/<int:anio>/<int:idestado>', views.Centros_acopio_agregar, name='centros_acopio_agregar'),
    path('centros/acopio/eliminar/<str:id>',views.centros_acopio_eliminar, name='centros_acopio_eliminar'),
    path('centros/acopio/editar/<str:id>/<int:anio>', views.centros_acopio_editar, name='centros_acopio_editar'),


    path('municipios',views.Municipios, name='municipios'),
    path('municipiosget', views.Municipios_consultar, name='municipiosget'),
    path('municipios/agregar/',views.municipios_agregar, name='municipios_agregar'),
    path('municipios/eliminar/<int:id>',views.Municipios_eliminar, name='municipios_eliminar'),
    path('municipios/editar/<int:id>', views.Municipios_editar, name='municipios_editar'),

    path('distritos',views.distritos, name='distritos'),
    path('distritos/agregar',views.distritos_agregar, name='distritos_agregar'),
    path('distritos/eliminar/<str:id>',views.distritos_eliminar, name='distritos_eliminar'),
    path('distritos/editar/<str:id>', views.distritos_editar, name='distritos_editar'),

    path('Tipo de Elección',views.Elecciones, name='elecciones_vista'),
    path('gettipo de Elección/<str:nombreeleccion>',views.Elecciones_consultar, name='getelecciones'),
    path('Tipo de Elección/agregar/<int:anio>',views.Elecciones_agregar, name='procesos_agregar'),
    path('Tipo de Elección/eliminar/<str:id>',views.Elecciones_eliminar, name='procesos_eliminar'),
    path('Tipo de Elección/editar/<str:id>', views.Elecciones_editar, name='procesos_editar'),
    path('Tipo de Elección/editar/cargos/<str:id>/<int:anio>/<int:idestado>', views.Elecciones_editar_cargos, name='procesos_editar_cargos'),
 
    path('docelecciones',views.docelecciones, name='docelecciones'),
    path('doceleccionesget/<str:nombreeleccion>',views.docelecciones_consulta, name='doceleccionesget'),
    path('docelecciones/agregar/<str:nombreeleccion>',views.docelecciones_agregar, name='docelecciones_agregar'),
    path('docelecciones/eliminar/<str:id>',views.docelecciones_eliminar, name='docelecciones_eliminar'),
    path('docelecciones/editar/<str:id>', views.docelecciones_editar, name='docelecciones_editar'),

    path('partidos/coaliciones',views.partidos_coaliciones, name='partidoscolas_coaliciones'), 
    path('partidos/coaliciones/get/',views.get_coaliciones_partidos, name='doceleccionesget'),
    path('partidos/coaliciones/agregar/<int:anio>',views.partidos_coaliciones_agregar, name='partidos_coaliciones_agregar'),
    path('partidos/coaliciones/eliminar/<str:id>',views.partidos_coaliciones_eliminar, name='partidos_coaliciones_eliminar'),
    path('partidos/coaliciones/editar/<str:id>', views.partidos_coaliciones_editar, name='partidos_coaliciones_editar'),

    path('Usuarios',views.Usuarios_Index, name='Usuarios_Index'), 
    path('Usuarios/get/<str:nombreelecion>/<int:idcargo>',views.consulta_usuarios, name='get_Usuarios'),
    path('Usuarios/agregar/<str:eleccion>/<int:idcargo>/<int:anio>',views.Usuarios_agregar, name='Usuarios_agregar'),
    path('Usuarios/eliminar/<str:id>',views.Usuarios_eliminar, name='Usuarios_eliminar'),
    path('Usuarios/editar/<str:id>', views.Usuarios_editar, name='Usuarios_editar'),


# URLS PARA REGISTRO DE CANDIATTURAS DE AYUNTAMIENTO  ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️

    path('Registro de Candidatura Ayuntamiento',views.regicand, name='regican'),
    path('Registro de Candidatura Ayuntamiento/<str:nombreeleccion>',views.docelecciones_consulta, name='regicanget'),
    path('Registro de Candidatura Ayuntamiento/get/',views.get_elecciones_Ayuntamiento, name='regicanday_geteleccion'),
    path('Registro de Candidatura Ayuntamiento/getyear/<int:anio>',views.get_eleccionefilter_ayuntamiento, name='regicanday_getyear'),
    path('Registro de Candidatura Ayuntamiento/consultar/<str:cargo>/<str:nombreeleccion>/<str:estado>/<str:anio>',views.regicadAy_consulta, name='regicanday_consultar'),
    path('regicandagregar/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:tipo>/<int:idpropietario>/<str:titulo>', views.agregar_AY_Propietario, name='regicandagregar'),
    path('regicandagregar/Sin Formula/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:tipo>/<int:municipio>', views.agregar_AY_sinfromula, name='regicandagregar'),
    path('eliminarcandAY/<int:id>', views.Eliminar_AY, name='eliminarcandAY'),
    path('editarcandAY/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Ay, name='editarcandAY'),
    path('editarcandAY/Suplente/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Ay_Suplente, name='editarcandAY_Suplente'),
    path('regicandagregar/Suplente/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:tipo>/<int:idpropietario>/<str:titulo>', views.agregar_AY_Suplente, name='regicandagregar_suplente'), 
    path('Documentos/candidatos/<int:id>/<str:nombreeleccion>/<str:nombrecargo>', views.documentos_candidatos, name='documentos_candidatos'),
    path('Documentos/candidatos/subir', views.carga_documentos, name='documentos_candidatos_subir'),
    path('visualizar_documento/', views.visualizar_documento, name='visualizar_documento'),


# URLS PARA REGISTRO DE CANDIATTURAS DE GOBERNADOR  ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️

    path('Registro de Candidatura Gubernatura',views.regicandgu, name='regicangu'),
    path('Registro de Candidatura Gu/get/',views.get_elecciones_Gu, name='regicanday_geteleccion'),
    path('Registro de Candidatura Gu/consultar/<int:cargo>/<str:nombreeleccion>/<int:id>',views.regicadGU_consulta, name='regicanday_geteleccion'),
    path('regicandagregar/gu/Sin Formula/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:tipo>/<int:idpropietario>', views.agregar_GU_sinfromula, name='regicandagregar'),
    path('Imprimir/reporte/<int:anio>/<str:nombreeleccion>/<str:idcargo>', views.Imprimir_reporte_global, name='Immprimir reporte global'),
    path('editarcandGU/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Gu, name='editarcandGU'),

# URLS PARA REGISTRO DE CANDIATTURAS DE RP ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️

path('Registro de Candidatura RP',views.regicanRP, name='regicanRP'),
path('Registro de Candidatura RP/get/',views.get_elecciones_Co, name='regicandco_geteleccion'),
path('Registro de Candidatura RP/get/my',views.get_elecciones_Co_My, name='regicandco_geteleccion'),
path('Registro de Candidatura RP/get/rp',views.get_elecciones_Co_Rp, name='regicandco_geteleccion'),
path('Registro de Candidatura RP/consultar/<str:cargo>/<str:eleccion>',views.regicadCO_RP_consulta, name='regicandco_geteleccion'),
path('regicandagregar/Co/Rp/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:tipo>/<int:idpropietario>/<str:titulo>/<int:distrito>', views.agregar_CO_RP_Propietario, name='regicandagregarrepresentacion'),
path('regicandagregar/Co/Rp/S/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:tipo>/<int:idpropietario>/<str:titulo>/<int:distrito>', views.agregar_CO_RP_Suplente, name='regicandagregarrepresentacion'),
path('editarcandCO/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Co, name='editarcandCO'),
path('editarcandCO/Suplente/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Co_Suplente, name='editarcandCO_Suplente'),
path('Registro de Candidatura RP/consultar/<int:cargo>/<str:nombreeleccion>/<int:id>',views.regicadRP_consulta, name='regicanday_geteleccion'),


# URLS PARA REGISTRO DE CANDIATTURAS DE MY ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
path('Registro de Candidatura MY',views.regicanMY, name='regicaMY'),
path('Registro de Candidatura MY/get/',views.get_elecciones_Co, name='regicandco_geteleccion'),
path('regicandagregar/Co/My/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:tipo>/<int:idpropietario>/<str:titulo>/<int:distrito>', views.agregar_CO_MY_Propietario, name='regicandagregarmayoria'),
path('Registro de Candidatura MY/consultar/<str:cargo>/<str:eleccion>',views.regicadCO_MY_consulta, name='regicandco_geteleccion'),
path('regicandagregar/Co/My/S/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:tipo>/<int:idpropietario>/<str:titulo>/<int:distrito>', views.agregar_CO_MY_Suplente, name='regicandagregarmayoria'),
path('editarcandMY/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Ay, name='editarcandAY'),
path('editarcandMY/Suplente/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Ay_Suplente, name='editarcandAY_Suplente'),
path('Registro de Candidatura MY/consultar/<int:cargo>/<str:nombreeleccion>/<int:id>',views.regicadMY_consulta, name='regicanday_geteleccion'),

# REVICION DEL OPLE ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️

path('Revicion_Ople',views.RevicionOple, name='RevicionOple'),
path('Revicion_Ople/get/',views.get_elecciones_All, name='regicandco_getall'),
path('Revicion_Ople/consultar/<int:cargo>/<str:nombreeleccion>/<int:id>',views.Revicion_Ople_All, name='regicandco_geteleccion'),
path('editarcandAY/Ople/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Ay_Ople, name='editarcandAY'),
path('Documentos/candidatos/Ople/<int:id>/<str:nombreeleccion>/<str:nombrecargo>/<int:anio>', views.documentos_candidatosOple, name='documentos_candidatos_Ople'),
path('comentar/documento/Ople/<int:id>/<str:iddoc>/<str:nombreeleccion>/<str:nombrecargo>/<int:anio>', views.comentar_documento, name='comentar_documento'),
path('editarcandGU/Ople/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Gu_Ople, name='Vizualizar_gu_ople'),
path('editarcandAY/Suplente/Ople/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Ay_Suplente_Ople, name='editarcandAY_Suplente_ople'),
path('editarcandCO/Ople/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Co_Ople, name='editarcandCO'),
path('editarcandCO/Suplente/Ople/<int:id>/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>', views.Editar_Co_Suplente_Ople, name='editarcandCO_Suplente_Ople'),

 # Sistema de Paquetes Electorales (Armado de Paquetes)
 path('Paquetes/Armado/',views.Paquetes_armado_index, name='Armado_Paquetes'),
 path('Paquetes/Armado/get/<str:eleccion>/<int:cargo>/<int:id>/<str:key>',views.get_paquetes_armados, name='get_paquetes_armados'),
 path('Paquetes/Armar/<str:eleccion>/<str:cargo>/<int:anio>/<str:valor>/<int:ide>',views.agregar_paquetes_armados, name='agregar_paquetes_armados'),
 path('Paquetes/Visualizar/<str:eleccion>/<str:cargo>/<str:num_paquete>/<int:anio>/<str:valor>/<int:folioc>',views.agregar_paquetes_vizualizar, name='agregar_paquetes_armados'),
 path('generar_pdf/Armado/Paquetes/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:idcand>', views.generar_pd_Armado_Paquetes, name='generar_pdf_armado_paquetes'),

 # Sistema de Paquetes Electorales (Entrega de Paquetes al CAE)
 path('Paquetes/Entrega/Cae',views.Paquetes_entrega_Cae_index, name='Entrega_Paquetes_CAE'),
 path('Paquxetes/Entrega/cae/get/<str:eleccion>/<int:cargo>/<int:id>/<str:key>',views.get_paquetes_entregados_cae, name='get_paquetes_entregados_cae'),
 path('Paquetes/Entregar/CAE/<str:eleccion>/<str:cargo>/<str:folioc>/<int:anio>/<str:valor>/<int:ide>',views.agregar_paquetes_entregados_cae, name='entregar_paquete_cae'),
 path('Paquetes/entrega/cae/Visualizar/<str:eleccion>/<str:cargo>/<str:folioc>/<int:anio>/<str:valor>/<int:ide>',views.entrega_paquetes_cae_vizualizar, name='entrega_paquetes_cae'),
 path('generar_pdf/Armado/Paquetes/entrega/cae/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:idcand>/<int:ide>', views.generar_pd_Entregado_Paquetes_cae, name='generar_pdf_entrega_cae_paquetes'),
# Sistema de Recepcion de paquetes (FASE 3)
 path('Paquetes/Entrega/Casilla',views.Paquetes_entrega_Casilla, name='Entrega_Paquetes_Casilla_index'),
 path('Paquxetes/Entrega/casilla/get/<str:eleccion>/<int:cargo>/<int:id>/<str:key>',views.get_paquetes_entregados_casilla, name='get_paquetes_entregados_casilla'),
 path('Paquetes/Entregar/casilla/<str:eleccion>/<str:cargo>/<str:folioc>/<int:anio>/<str:valor>/<int:ide>',views.agregar_paquetes_entregados_casillas, name='entregar_paquete_casilla'),
 path('Paquetes/entrega/casilla/Visualizar/<str:eleccion>/<str:cargo>/<str:folioc>/<int:anio>/<str:valor>/<int:ide>',views.Vizualizar_paquetes_entregados_casillas, name='entrega_paquetes_casilla'),
 path('generar_pdf/Armado/Paquetes/entrega/casilla/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:idcand>/<int:ide>', views.generar_pd_Entregado_Paquetes_casilla, name='generar_pdf_entrega_cae_paquetes'),
# Sistema de Recoleccion de Paquetes (FASE 4)
 path('Paquetes/Entrega/Casilla/Recoleccion',views.Paquetes_recoleccion_Casilla, name='Entrega_Paquetes_Casilla_Recoleccion'),
 path('Paquxetes/verificacion/estatus/<str:id>/',views.verificar_estatus_paquete, name='get_paquetes_verificar_estatus'),
 path('Paquxetes/Entrega/casilla/get/recoleccion/<str:eleccion>/<int:cargo>/<int:id>/<str:key>',views.get_paquetes_recolectados_casilla, name='get_paquetes_entregados_casilla_recoleccion'),
 path('Paquetes/Entregar/en/casilla/recoleccion/<str:eleccion>/<str:cargo>/<str:folioc>/<int:anio>/<str:valor>/<int:ide>',views.agregar_paquetes_recolectados_casillasbeta, name='entregar_paquete_casilla_recoleccion'),
 path('Paquetes/entregados/en/casilla/Visualizar/recolectados/<str:eleccion>/<str:cargo>/<str:folioc>/<int:anio>/<str:valor>/<int:ide>',views.agregar_paquetes_recolectados_casillasbeta_viwes, name='entrega_paquetes_casilla_Visualizar_recolectados'),
 path('generar_pdf/Armado/Paquetes/entrega/casilla/recoleccion/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<str:idcand>/<int:ide>', views.generar_pd_Entregado_Paquetes_recoleccion, name='generar_pdf_entrega_cae_paquetes'),
#resumen de paquetes electorales
 path('Paquetes/Resumen',views.Resumen_de_paquetes, name='Resumen_de_paquetes'),
 path('Paquxetes/Entrega/casilla/get/recoleccion/all/<str:eleccion>/<int:cargo>/<int:id>/<str:key>',views.get_paquetes_recolectados_casilla_all, name='get_paquetes_entregados_casilla_recoleccion'),

 # Recorrido de Paquetes
 path('Paquetes/Recorrido',views.Recorrido_de_paquetes, name='Recorrido_de_paquetes'),
 path('Paquxetes/Recorrido/casilla/get/recoleccion/<str:eleccion>/<str:cargo>/<int:id>/<str:key>',views.get_paquetes_recorrido_casilla, name='get_paquetes_entregados_casilla_recorrido'),
 path('Paquetes/Recorrido/Visualizar/<int:id_paquetetranslado>/<str:estado>/<int:anio>/<str:eleccion>/<str:cargo>/<int:paqueteid>', views.Recorrido_de_paquetes_editar, name='Recorrido_de_paquetes_visualizar'),
 path('Paquetes/Recorrido/<str:latitud>/<str:longitud>/', views.Ubicar_paquete, name='ubicar_paquete'),
# Sistema de Representantes para computos
 path('Computos/Agregar/Candidatos/',views.Computos_Agrecand_index, name='Comp_Agregar_Candidatos_Agregar'),
 path('get/representantes/<int:anio>/<str:nombreeleccion>/<str:cargo>',views.get_representantes_computos, name='get_representates'),
 path('agregar/representantes/<int:anio>/<str:nombreeleccion>/<str:cargo>',views.agregar_Representantes_Titulares_Computos, name='agregar_representates'),
 path('editar/representantes/<int:id>/<str:eleccion>/<str:cargo>/<int:anio>',views.agregar_Representantes_editar_titular, name='editar_representates_titulares'),
 path('eliminar/representantes/<int:id>/',views.agregar_Representantes_eliminar, name='eliminar_representates_titulares'),
 path('Documentos/representantes/<int:id>/<str:nombreeleccion>/<int:anio>/<str:cargo>', views.documentos_representantes, name='documentos_representantes'),
 path('Documentos/representantes/subir', views.carga_documentos_representantes, name='documentos_representantes_subir'),
 path('visualizar_documento/representantes', views.visualizar_documento_representantes, name='visualizar_documento_representantes'),
 path('generar_pdf/Representantes/<str:anio>/<str:nombreeleccion>/<str:idcand>/<str:cargo>', views.generar_pd_Representante, name='generar_pdf_Representantes'),
#Representantes Ople
 path('Computos/Representantes/',views.Rerepre_Ople_index, name='representantes_Ople'),
 path('get/representantes/<int:anio>/<str:nombreeleccion>/<str:cargo>/<int:partido>',views.get_representantes_Ople, name='get_representates'),
 path('Vizualizar/representantes/Ople/<int:id>/<str:eleccion>/<str:cargo>/<int:anio>',views.agregar_Representantes_editar_titular_Ople, name='editar_representates_titulares'),
# Sistema de Observadores
 path('Observadores/Agregar/Observadores/',views.Observadores_Agre_index, name='Observadores_index'),
 path('get/Observadores/<int:anio>/<str:nombreeleccion>/<str:cargo>',views.get_Observadores, name='get_Observadores'),
 path('agregar/Observadores/<int:anio>/<str:nombreeleccion>/<str:cargo>',views.agregar_Observadores, name='agregar_Observadores'),
 path('editar/Observadores/<int:id>/<str:eleccion>/<str:cargo>/<int:anio>',views.agregar_Observadores_editar, name='editar_Observadores'),
 path('eliminar/Observadores/<int:id>/',views.Observadores_eliminar, name='eliminar_observadores'),
  path('Documentos/Observadores/<int:id>/<str:nombreeleccion>/<int:anio>/<str:cargo>', views.documentos_Observadores, name='documentos_Observadores'),
# Sistema de Registro de Candidatura de Mayoria Rekativa (Congreso)
    path('Registro de Diputaciones de Mayoria',views.regicad_my, name='regicanmy'),
    path('Registro de Candidatura Congreso/get/',views.get_elecciones_Congreso, name='regicandco_geteleccion'),
    path('Registro de Diputaciones de Mayoria/<str:nombreeleccion>',views.docelecciones_consulta, name='regicanmyget'),
    path('Registro de Candidatura Congreso/getyear/<int:anio>',views.get_eleccionefilter_congreso, name='regicanday_getyear'),
    path('Registro de Candidatura Congreso/consultar/<int:iddistrito>/<str:nombreeleccion>',views.regicadCo_consulta, name='regicandcongreso_consultar'),
# Sistema de Computos (Integrar Candidatos)
    path('Candidatos en Contienda',views.candidatos_contienda, name='candidatos_contienda'),
    path('get/Candidatos/en/contienda/<int:anio>/<str:nombreeleccion>/<str:cargo>',views.get_Candidatos_Contienda, name='get_candidatos_en_contienda'),
    path('Candidatos/en/contienda/Integrar/<int:anio>/<str:nombreeleccion>/<str:cargo>',views.Integrar_Candidatos, name='Integrar_Candidatos'),
    path('Candidatos/en/contienda/foto/subir', views.carga_foto_candidato, name='Foto_candidatos_subir'),
    path('Candidatos/en/contienda/Integrar/<int:idcand>', views.Integrar_candidato_Eleccion, name='Foto_candidatos_subir'),
    path('Candidatos/en/contienda/dar/baja/<int:id>/', views.Candidatos_contienda_eliminar, name='candidatos_contienda_eliminar'),
# Sistema de Computos (Computo de votos )
    path('Computo de Votos',views.computo_votos, name='comp_votos'),
    path('get/Paquete/no/contado/<int:anio>/<str:nombreeleccion>/<str:cargo>/<str:folioc>',views.Paquete_numero_cero, name='get_Paquete_no_contado'),
    path('guardar_datos/', views.guardar_datos, name='guardar_datos'),



# Sistema de Porcentajes de Avances 
    path('Porcentajes de Avances ',views.porcentajes_Avances, name='porcentajes de Avances'),
    path('pruba/consulta', views.prueba_consulta, name='queso'),
    path('conteo/actas/<int:idcargo>/<str:nombreeleccion>', views.ConteodeActas, name='get_conteo de actas'),


# Sostema de Votos por Partido
    path('Votos por Partido',views.votos_partido, name='votos_partido'),




# Sistema de Resumend de Actas
    path('Resumen de Actas',views.Resumen_actas, name='Resumen de Actas'),
    path('Resumen de Actas/Consulta/<int:idproceso>/<int:idtipocargo>',views.Resumen_actas_consultar, name='Resumen de Actas Consulta'),





    #path('docelecciones/agregar/<str:nombreeleccion>',views.docelecciones_agregar, name='docelecciones_agregar'),
    #path('docelecciones/eliminar/<str:id>',views.docelecciones_eliminar, name='docelecciones_eliminar'),
    #path('docelecciones/editar/<str:id>', views.docelecciones_editar, name='docelecciones_editar'),








    path('generar_pdf/<int:anio>/<str:nombreeleccion>/<str:nombrecargo>/<int:idcand>', views.generar_pdf, name='generar_pdf'),
    path('elecciones/', views.get_elecciones, name='get_elecciones'),
    path('estados/', views.get_estados, name='get_estados'),
    path('partidos/', views.get_partidos, name='get_partidos'),
    path('consejos/', views.get_consejos, name='get_consejos'),
    path('cargos/<str:idproceso>', views.get_cargos, name='get_cargos'),
    path('cargos/filter/<str:idproceso>/<str:idtipocargo>', views. get_cargos_filter, name='get_cargos'),
    path('casillas/<str:idtipoc_id>/<str:eleccion>/<int:iddis>', views.get_casillas, name='get_casillas'),
    path('eleccionesfilter/<int:anio>', views.get_eleccionefilter, name='get_eleccionesfilter'),
    path('getdistritos/<int:idestado>', views.get_distritos, name='get_distritos'),
    path('<int:id>', views.get_municipios, name='get_municipios'),
    path('getcoalicioens/<int:id>', views.get_coaliciones, name='get_coalicioens'),
    path('filtrarmunicipiospordistrito/<int:iddistrito>',views.get_municipios_distrito, name='get_municipiospordistrito'),

    path('tobase64',views.prueba_guardar_imagen, name='siuu'),
    path('NumeroEleccion/<int:idproceso>/<int:idtipocargo>',views.get_num_elec, name='Num_elec'),

    # SERVICIOS PARA APLICACION MOVIL
    path('Site/PaquetesElectorales.WebApi/Login', views.check_password, name='check_password'),
    path('Site/PaquetesElectorales.WebApi/SaveTransfer', views.save_transfer_rqt, name='save_transfer_rqt'),
    path('Site/PaquetesElectorales.WebApi/registerRoute', views.register_route_rqt, name='register_route_rqt'),
    path('Site/PaquetesElectorales.WebApi/ArrivalPackage', views.deliver_package_rqt, name='deliver_package_rqt'),
    path('Site/PaquetesElectorales.WebApi/DeliveryPackage', views.deliver_package, name='deliver_package'),
    path('Site/PaquetesElectorales.WebApi/UpdateCredentials', views.UpdateCredentials, name='UpdateCredentials'),
    path('Site/PaquetesElectorales.WebApi/SaveIncident', views.SaveIncident, name='SaveIncident'),
    path('Site/PaquetesElectorales.WebApi/Reset', views.reset_packages, name='ResetPackages'),
    path('Site/PaquetesElectorales.WebApi/Get/Paquetes', views.obtener_paquetes_por_uduario, name='Get_Paquetes'),
    path('Site/PaquetesElectorales.WebApi/Get/Estatus/Paquetes/Usuario', views.obtener_estatus_paquete_por_uduario, name='Get_Paquetes'),
    path('Site/PaquetesElectorales.WebApi/Get/Incidencias', views.obtener_paquetes_por_uduario_incidencia, name='Get_Route'),
    path('Site/PaquetesElectorales.WebApi/CerrarSessions', views.desactivar_usuario, name="CerrarSessions")


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)