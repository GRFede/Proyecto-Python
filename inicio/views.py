from django.http import HttpResponse

def inicio(request):
    return HttpResponse('<h1> Soy la pantalla de inicio</h1>') #Se pueden colocar
#las etiquetas pero hay una forma mas rapida de configurarlo que lo vemos mas adelante.
def vista_datos1(request,nombre):
    nombre_mayuscula=nombre.upper()#upper() es una funcion para poner en mayuscula el nombre.
    return HttpResponse(f'Hola {nombre_mayuscula}!!!')