# usuarios/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page
    else:
        form = UserCreationForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})