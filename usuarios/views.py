from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenido/a {user.first_name}! Registro exitoso.')
            return redirect('pagina_principal')  # Cambiar por tu vista principal
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido/a {user.first_name or user.username}!')
            return redirect('pagina_principal')  # Cambiar por tu vista principal
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'usuarios/login.html')