from django.shortcuts import render, redirect
from .forms import CartForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def CartDetails(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            movie_name = form.cleaned_data.get('movie_name')
            messages.success(request, f'Your movie '+movie_name+' has been requested! It will be posted soon.')
    else:
        form = CartForm()
    return render(request, 'cart/cart.html', {'form': form})