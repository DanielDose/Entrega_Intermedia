from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppEmpresa.models import Empresa, Area, Trabajador
from AppEmpresa.forms import EmpresaFormulario, AreaFormulario, TrabajadorFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.

def inicio(request):

      return render(request, "AppEmpresa/inicio.html")


def empresa(request):
    
      return render(request, "AppEmpresa/empresa.html")


# def empresaFormulario(request):

#       if request.method == 'POST':

#             empresa = Empresa ( request.POST['empresa'])
#             empresa.save()

#             return render(request, "AppEmpresa/inicio.html")

#       return render(request, "AppEmpresa/empresaFormulario.html")

# def empresaFormularioSimple(request):

#       return render(request, "AppEmpresa/empresaFormularioSimple.html")


def area(request):

      return render(request, "AppEmpresa/area.html")


def trabajador(request):

      return render(request, "AppEmpresa/trabajador.html")


def empresaFormulario(request):

      if request.method == 'POST':

            miFormulario1 = EmpresaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario1)

            if miFormulario1.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario1.cleaned_data

                  empresa = Empresa(nombre_empresa=informacion['nombre_empresa']) 

                  empresa.save()

                  return render(request, "AppEmpresa/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario1= EmpresaFormulario() #Formulario vacio para construir el html

      return render(request, "AppEmpresa/empresa.html", {"miFormulario1":miFormulario1})

def areaFormulario(request):

      if request.method == 'POST':

            miFormulario2 = AreaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario2)

            if miFormulario2.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario2.cleaned_data

                  area = Area(nombre_area=informacion['nombre_area'], cantidad_empleados=informacion['cantidad_empleados']) 

                  area.save()

                  return render(request, "AppEmpresa/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario2= AreaFormulario() #Formulario vacio para construir el html

      return render(request, "AppEmpresa/area.html", {"miFormulario2":miFormulario2})


def trabajadorFormulario(request):

      if request.method == 'POST':

            miFormulario3 = TrabajadorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario3)

            if miFormulario3.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario3.cleaned_data

                  trabajador = Trabajador(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion']) 

                  trabajador.save()

                  return render(request, "AppEmpresa/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario3= TrabajadorFormulario() #Formulario vacio para construir el html

      return render(request, "AppEmpresa/trabajador.html", {"miFormulario3":miFormulario3})


# def busquedaProfesion(request):

#       return render(request, "AppEmpresa/busquedaProfesion.html")


def buscar(request):

      if request.GET["profesion"]:

            profesion = request.GET['profesion']
            print(profesion)
            emails = Trabajador.objects.filter(profesion__icontains=profesion)
            print(emails)
            return render(request, "AppEmpresa/inicio.html", {"emails":emails, "profesion":profesion})
      
      else:

            respuesta = "no enviaste datos"

      return render(request, "AppEmpresa/inicio.html", {"respuesta":respuesta})
# def buscar(request):

#       respuesta = f"estoy buscando la profesion: {request.GET['profesion']}"

#       return HttpResponse(respuesta)

#def profesores(request):

#       if request.method == 'POST':

#             miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

#             print(miFormulario)

#             if miFormulario.is_valid:   #Si pasó la validación de Django

#                   informacion = miFormulario.cleaned_data

#                   profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
#                    email=informacion['email'], profesion=informacion['profesion']) 

#                   profesor.save()

#                   return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

#       else: 

#             miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

#       return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})






# def buscar(request):

#       if  request.GET["camada"]:

# 	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
#             camada = request.GET['camada'] 
#             cursos = Curso.objects.filter(camada__icontains=camada)

#             return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

#       else: 

# 	      respuesta = "No enviaste datos"

#       #No olvidar from django.http import HttpResponse
#       return HttpResponse(respuesta)



# def leerProfesores(request):

#       profesores = Profesor.objects.all() #trae todos los profesores

#       contexto= {"profesores":profesores} 

#       return render(request, "AppCoder/leerProfesores.html",contexto)



# def eliminarProfesor(request, profesor_nombre):

#       profesor = Profesor.objects.get(nombre=profesor_nombre)
#       profesor.delete()
      
#       #vuelvo al menú
#       profesores = Profesor.objects.all() #trae todos los profesores

#       contexto= {"profesores":profesores} 

#       return render(request, "AppCoder/leerProfesores.html",contexto)



# def editarProfesor(request, profesor_nombre):

#       #Recibe el nombre del profesor que vamos a modificar
#       profesor = Profesor.objects.get(nombre=profesor_nombre)

#       #Si es metodo POST hago lo mismo que el agregar
#       if request.method == 'POST':

#             miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

#             print(miFormulario)

#             if miFormulario.is_valid:   #Si pasó la validación de Django

#                   informacion = miFormulario.cleaned_data

#                   profesor.nombre = informacion['nombre']
#                   profesor.apellido = informacion['apellido']
#                   profesor.email = informacion['email']
#                   profesor.profesion = informacion['profesion']

#                   profesor.save()

#                   return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
#       #En caso que no sea post
#       else: 
#             #Creo el formulario con los datos que voy a modificar
#             miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
#             'email':profesor.email, 'profesion':profesor.profesion}) 

#       #Voy al html que me permite editar
#       return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})




# class CursoList(ListView):

#       model = Curso 
#       template_name = "AppCoder/cursos_list.html"



# class CursoDetalle(DetailView):

#       model = Curso
#       template_name = "AppCoder/curso_detalle.html"



# class CursoCreacion(CreateView):

#       model = Curso
#       success_url = "/AppCoder/curso/list"
#       fields = ['nombre', 'camada']


# class CursoUpdate(UpdateView):

#       model = Curso
#       success_url = "/AppCoder/curso/list"
#       fields  = ['nombre', 'camada']


# class CursoDelete(DeleteView):

#       model = Curso
#       success_url = "/AppCoder/curso/list"
     