from django.shortcuts import render, redirect
from .forms import CartForm
# Create your views here.

def CartDetails(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            movie_name = form.cleaned_data.get('movie_name')
            return redirect('login')
    else:
        form = CartForm()
    return render(request, 'cart/cart.html', {'form': form})