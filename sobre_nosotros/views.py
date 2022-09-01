from django.shortcuts import render


# Create your views here.
def sobrenos(request):
    return render(request, "sobre_nosotros.html")
