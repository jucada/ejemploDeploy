from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos/", curso, name="Curso"),
    path("profesores/", profesor, name="Profesores"),
    path("estudiantes/", estudiante, name="Estudiantes"),
    path("entregables/", entregable, name="Entregables"),
    path("cursoFormulario/", cursoFormulario, name="FormularioCurso"),
    path("buscarCamada/", busquedaCamada, name="BuscarCamada"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    path("login/", inicioSesion, name="Login"),
    path("register/", registro, name="SignUp"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar/", agregarAvatar, name="Avatar"),


    #CRUD de profesores 
    path("leerProfes/", leerProfesores, name="ProfesoresLeer"),
    path("crearProfes/", crearProfesores, name="ProfesoresCrear"),
    path("eliminarProfes/<profeNombre>/", eliminarProfesores, name="ProfesoresEliminar"),
    path("editarProfes/<profeNombre>/", editarProfesores, name="ProfesoresEditar"),


    #CRUD de Cursos usando Clases

    path("curso/list/", ListaCurso.as_view(), name="CursosLeer"),
    path("curso/<int:pk>", DetalleCurso.as_view(), name="CursosDetalle"),
    path("curso/crear/", CrearCurso.as_view(), name="CursosCrear"),
    path("curso/editar/<int:pk>", ActualizarCurso.as_view(), name="CursosEditar"),
    path("curso/borrar/<int:pk>", BorrarCurso.as_view(), name="CursosBorrar"),

]
