from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from inicio.models import Auto, Persona

def inicio (request):
    #return HttpResponse('<h1> Soy la pantalla de inicio</h1>') #Se pueden colocar
#las etiquetas pero hay una forma mas rapida de configurarlo que lo vemos mas adelante.

    return render(request, 'index.html')
    
def vista_datos1(request,nombre):
    nombre_mayuscula=nombre.upper()#upper() es una funcion para poner en mayuscula el nombre.
    return HttpResponse(f'Hola {nombre_mayuscula}!!!')

def primer_template(request):

    #sin with
    #archivo_del_template = open(r'Template\primer_template.html')
    #template = Template(archivo_del_template.read())
    #archivo_del_template.close()
    #contexto = Context()

    #render_template = template.render(contexto)

    #con with
    with open(r'Template\primer_template.html') as archivo_del_template:
        template = Template(archivo_del_template.read())
        
    contexto = Context()

    render_template = template.render(contexto)

    return HttpResponse(render_template)

def segundo_template(request):

    fecha_actual = datetime.now()
    datos = {   
    'fecha_actual': fecha_actual
    }

    #v1
    #with open(r'Template\segundo_template.html') as archivo_del_template:
    #    template = Template(archivo_del_template.read())
    #contexto = Context(datos)
    #render_template = template.render(contexto)
    #return HttpResponse(render_template)

    #v2
    #template = loader.get_template('segundo_template.html')
    #render_template = template.render(datos)
    #return HttpResponse(render_template)

    #v3
    return render(request, 'segundo_template.html', datos)

def creando_auto(request):

    auto = Auto(marca='Ford', modelo="Focus", anio=2014)
    auto.save()

    return render(request, 'creando_auto.html', {})

def agrego_personas(request):

    persona = Persona(Nombre='Federico', apellido="Garcia", edad=33)
    persona.save()

    return render(request, 'agrego_personas.html', {})