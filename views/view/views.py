from turtle import clear

from .models import info
from .forms import infoForm
from django.contrib import messages
from django.shortcuts import redirect, render

def info_view(request):
    info_data = info.objects.all()

    
    if request.method == 'POST':
        form = infoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form submitted successfully")
            return redirect('info') # help to prevent resubmission of form on page refresh
        else:
            messages.error(request, "Form is not valid")

    context = {
        'form': infoForm(),
        'info_data': info_data
    }
    return render(request, 'info.html', context)