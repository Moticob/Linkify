from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import pyshorteners

def url_shortener(request):
    try:
        short_url = ""
        url = ""
        if request.method == "POST":
            shortener = pyshorteners.Shortener()
            url = request.POST.get("url")
            short_url = shortener.tinyurl.short(url)
            messages.success(request, "Generated")
        return render(
            request, "url-shortener.html", {"short_url": short_url, "url": url}
        )
    except:
        # Ajout d'un message d'erreur
        messages.error(request, "An error occurred")
        return render(request, "url-shortener.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger l'utilisateur vers une page de confirmation ou de connexion
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
