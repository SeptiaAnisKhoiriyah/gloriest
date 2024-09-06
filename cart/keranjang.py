from decimal import Decimal
from django.conf import settings
from website.models import Bahan


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, bahan, quantity=1, update_quantity=False):
        bahan_id = str(bahan.id)
        if bahan_id not in self.cart:
            self.cart[bahan_id] = {'quantity': 0, 'price': int(bahan.setela_diskon)}
        if update_quantity:
            self.cart[bahan_id]['quantity'] = quantity
        else:
            self.cart[bahan_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, bahan):
        bahan_id = str(bahan.id)
        if bahan_id in self.cart:
            del self.cart[bahan_id]
            self.save()

    def __iter__(self):
        bahan_ids = self.cart.keys()
        bahans = Bahan.objects.filter(id__in=bahan_ids)
        for bahan in bahans:
            self.cart[str(bahan.id)]['bahan'] = bahan

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
