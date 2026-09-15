from django.shortcuts import render, redirect # Se importa la funcion render y redirect que ofrece django
from django.contrib.auth import authenticate, login# Se importa la funcion authenticate que ofrece django


# Funcion que renderiza el html de la app publica
def index(request):
    return render(request, 'public_app/index.html')

# Funcion que renderiza el html del login
def login_view(request):
    
    # request es un objeto con propiedades
    # Si el usuario presiona el botón "Entrar" del forms, la petición es POST y entra el condicional
    if request.method == 'POST':
        # Guarda los datos que vienen de los inputs del HTML 
        # Al hacer el metodo POST se crea un diccionario llamado "request.POST = { }" con los datos del forms (django hace esto)
        # Se usa el metodo .get para evitar el KeyError y se detenga la app
        usuario_ingresado = request.POST.get('username')
        clave_ingresada = request.POST.get('password')

        # Consulta contra la Base de Datos usando la funcion authenticate hecha por django.
        # Si la persona existe y la contraseña coincide, regresa un objeto con los datos del usuario
        # Si las credenciales no coinciden o no existe, regresa None.
        user = authenticate(request, username = usuario_ingresado, password = clave_ingresada)

        # Evalua si se redirige o no a la pagina privada
        if user is not None:
            # Si las credenciales son correctas se inicia sesión y guarda los datos para persistencia
            login(request, user)
            return redirect('private_index') # Usa el alias name ' ' (Concatena el path implicitamente)
        else:
            # Credenciales incorrectas, regresa al login con un mensaje de error
            # En forma de diccionario como "error" como clave (formato aceptado para envio y recepccion)
            # Django formatea el diccinoario pasa de clave : valor a variable = valor
            return render(request, 'public_app/login.html', {
                "error": "Usuario o contraseña incorrectos. Intentalo de nuevo"
            })

    # Si el usuario ya hizo el login se perserva su sesion
    if request.user.is_authenticated: # Regresa True o False (ID de sesion)
        return redirect('private_index')
        
    # Se entra por primera vez al formulario (usa el metodo GET)
    return render(request, 'public_app/login.html')