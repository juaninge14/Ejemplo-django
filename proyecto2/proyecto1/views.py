from django.http import HttpResponse
import datetime

#def saludar(request):
#    return HttpResponse ("Hola de nuevo, aca estamos escribiendo python en Django")

#def despedir(request):
#    return HttpResponse ("Nos vemos, hasta luego !")

def ver_fecha(request):
    fecha_actual = datetime.datetime.now()

    contenido_texto = """ <html>

    <body style="background-color: lightsalmon;">
    <h1> Aqui veremos el cambio de horario y fecha %s </h1>
    </body>

    </html> """ % fecha_actual
    return HttpResponse (contenido_texto)

