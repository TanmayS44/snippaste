from django.shortcuts import render, redirect

from django.http import HttpResponse

from.forms import PasteForm
from .models import Snippet

# Create your views here.
def index(request):
    return render(request, "index.html")

def create_snippet(request):
    if request.method == "POST":
        form = PasteForm(request.POST)
        if form.is_valid():
            new_snippet = form.save(commit=False)
            new_snippet.save()
            return redirect("view_snippet", snippet_id=new_snippet.id)
    else:
        form = PasteForm
    return render(request, "create_snippet.html", {"form": form})

def view_snippet(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    return render(request, "snippet_details.html", {"snippet": snippet})
