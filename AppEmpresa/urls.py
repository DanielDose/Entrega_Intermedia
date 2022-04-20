from django.urls import path

from AppEmpresa import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"),
    path('Empresa', views.empresa, name="Empresa"),
    path('Area', views.area, name="Area"),
    path('Trabajador', views.trabajador, name="Trabajador"),
    path('empresaFormulario', views.empresaFormulario, name="empresaFormulario"),
    path('areaFormulario', views.areaFormulario, name="areaFormulario"),
    path('trabajadorFormulario', views.trabajadorFormulario, name="trabajadorFormulario"),
    # path('busquedaProfesion', views.busquedaProfesion, name="busquedaProfesion"),
    path('buscar/', views.buscar),
    # path('empresaFormularioSimple', views.empresaFormulario, name="empresaFormularioSimple"),
    # path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    # path('buscar/', views.buscar),
    # path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
    # path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    # path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),


    # path('curso/list', views.CursoList.as_view(), name='List'),
    # path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    # path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    # path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    # path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),

    #path(r'^$', views.CursoList.as_view(), name='list'),
    #path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='detail'),
    #path(r'^nuevo$', views.CursoCreacion.as_view(), name='new'),
    #path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='edit'),
    #path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='delete'),

]

