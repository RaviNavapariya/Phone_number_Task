from audioop import reverse
from django.shortcuts import render, redirect
from .forms import PhoneNumberForm
# Create your views here.
def phonenumber(request):
    if request.method == "POST":
        form = PhoneNumberForm(request.POST)
        print("___________________________________",form)
        if form.is_valid():
            form.save()
            return redirect(reverse('base'))
        form = PhoneNumberForm
        return render(request, 'base.html', {'form':form})

    form = PhoneNumberForm()
    return render(request, 'base.html', {'form':form})