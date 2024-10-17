from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime

def inicio(request):
    return HttpResponse('<h1> Soy la pantalla de inicio</h1>') #Se pueden colocar
#las etiquetas pero hay una forma mas rapida de configurarlo que lo vemos mas adelante.
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

    with open(r'Template\segundo_template.html') as archivo_del_template:
        template = Template(archivo_del_template.read())
    
    datos = {   
    'fecha_actual': fecha_actual
    }

    contexto = Context(datos)

    render_template = template.render(contexto)

    return HttpResponse(render_template)