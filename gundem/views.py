from django.shortcuts import render

# Create your views here.
def gundem(request):
    return render(request, "gundem.html")