from django.shortcuts import render

# Create your views here.

def all_collaborators(request):
    return render(request, "collaborators/all_collaborators.html")