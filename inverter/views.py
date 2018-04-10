from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import InvertImageForm
from .models import *

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        )
def uploadFile(request, pk):
    file_inst = get_object_or_404(FileInstance, pk=pk)

    if request.method == 'GET':
        form = InvertImageForm(initial={})
    elif request.method == 'POST':
        form = InvertImageForm(request.POST)
        book_inst.save()
        return HttpResponseRedirect(reverse('image uploaded'))
        
    return render(
        request,
        'index.html',
        {'form': form, 'fileinst': file_inst}
        )

    
