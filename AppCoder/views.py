from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import Curso, Profesor
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.



def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user:

                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {user}"})

        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos."})

    else:

        form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"formulario":form})


def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario creado."})
    
    else:

        form = UsuarioRegistro()

    return render(request, "AppCoder/registro.html", {"formulario":form})

@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })

    return render(request, "AppCoder/editarPerfil.html", {"formulario":form, "usuario":usuario})

def inicio(request):
    return render(request,"AppCoder/inicio.html", {"mensaje":"Bienvenido a mi página web!"})

def curso(request):

    cur1 = Curso(nombre="Desarrollo Web", camada=1111)
    cur1.save()

    return HttpResponse(f"El curso que ha creado es: {cur1.nombre} y su camada es: {cur1.camada}.")

def estudiante(request):

    return render(request,"AppCoder/estudiantes.html")

def profesor(request):

    return render(request,"AppCoder/profesores.html")

def entregable(request):

    return render(request,"AppCoder/entregables.html")

def cursoFormulario(request):

    if request.method == "POST":    #despues de dar click al botón enviar

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            curso = Curso(nombre=info["curso"], camada=info["camada"])

            curso.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})


def busquedaCamada(request):

    return render(request, "AppCoder/inicio.html")

def resultados(request):

    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__iexact=camada)

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)

@login_required
def leerProfesores(request):
    
    profesores = Profesor.objects.all()

    contexto = {"teachers": profesores}

    return render(request, "AppCoder/leerProfes.html", contexto)


def crearProfesores(request):

    if request.method == "POST":    #despues de dar click al botón enviar

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            profesor = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])

            profesor.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = ProfesorFormulario()

    return render(request, "AppCoder/profeFormulario.html", {"miFormulario":miFormulario})

def eliminarProfesores(request, profeNombre):

    profesor = Profesor.objects.get(nombre=profeNombre)
    profesor.delete()

    profesores = Profesor.objects.all()

    contexto = {"teachers":profesores}

    return render(request, "AppCoder/leerProfes.html", contexto)



def editarProfesores(request, profeNombre):

    profesor = Profesor.objects.get(nombre=profeNombre)

    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            profesor.nombre = info["nombre"]
            profesor.apellido = info["apellido"]
            profesor.email = info["email"]
            profesor.profesion = info["profesion"]

            profesor.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = ProfesorFormulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido,
        "email":profesor.email, "profesion":profesor.profesion})

    return render(request, "AppCoder/editarProfe.html", {"miFormulario":miFormulario, "nombre":profeNombre})



@login_required
def agregarAvatar(request):

    if request.method=="POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user) 

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form = AvatarFormulario()

    return render(request, "AppCoder/agregarAvatar.html", {"formulario":form})



class ListaCurso(LoginRequiredMixin, ListView):

    model = Curso

class DetalleCurso(LoginRequiredMixin, DetailView):

    model = Curso

class CrearCurso(LoginRequiredMixin, CreateView):

    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "camada"]

class ActualizarCurso(LoginRequiredMixin, UpdateView):
    
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ["nombre", "camada"]

class BorrarCurso(LoginRequiredMixin, DeleteView):

    model = Curso
    success_url = "/AppCoder/curso/list"
