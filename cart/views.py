# import json
# import datetime
# import urllib.request
# from django.conf import settings
# from django.views.generic import View
# from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from website.models import Bahan
from .models import Transaksi, DetailTransaksi
from .keranjang import Cart
from .forms import CartAddBahanForm
from django.contrib.auth.decorators import login_required
from website.decorators import ijinkan_pengguna,pilihan_login

@require_POST
def cart_add(request, bahan_id):
    cart = Cart(request)  # create a new cart object passing it the request object 
    bahan = get_object_or_404(Bahan, id=bahan_id) 
    quantity = int(request.POST.get('quantity'))
    form = CartAddBahanForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(bahan=bahan, quantity=quantity, update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, bahan_id):
    cart = Cart(request)
    bahan = get_object_or_404(Bahan, id=bahan_id)
    cart.remove(bahan)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    context = {
            'judul': 'Halaman Cart',
            'cart':cart
        }
    
    for item in cart:
        item['update_quantity_form'] = CartAddBahanForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request,'pemesanan.html',context)

