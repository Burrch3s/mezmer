from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import InvertImageForm
from .models import *

# Create your views here.
def index(request):
    #file_inst = get_object_or_404(FileInstance, pk=pk)
    file_inst = FileInstance()
    images = FileInstance.objects.all()
    print(images)

    if request.method == 'POST':
        form = InvertImageForm(request.POST, request.FILES)
        file_inst.save()
        print("[*] Saving the picture!")
        #return HttpResponseRedirect(reverse('/'))

    else:
        form = InvertImageForm(initial={})

    return render(request, 'index.html', {'form': form, 'fileinst':file_inst, 'images':images})
