from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message  # importer ton modèle Message

def home(request):
    form = MessageForm()
    nom = None
    message = None
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            nom = form.cleaned_data['nom']
            message = form.cleaned_data['message']
            # redirection après la sauvegarde pour éviter la double soumission
            return redirect('home')

    # Récupérer les messages triés du plus récent au plus ancien
    messages = Message.objects.all().order_by('-date')

    return render(request, 'accueil/home.html', {
        'form': form,
        'nom': nom,
        'message': message,
        'messages': messages
    })
