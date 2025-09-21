from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            login(request,u)
            return redirect('product_list')
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})
