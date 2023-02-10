from django.shortcuts import render, redirect
import stripe
from django.conf import settings
from stripe_app.models import Item


def get_item(request, id):
    items = Item.objects.all()
    return render(request, 'stripe_app/index.html', {'items': items})


stripe.api_key = settings.STRIPE_SECRET_KEY


def buy(request):
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price': 'price_1MZyk0F8Hswxyi6ssv8VDLTF',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://localhost:8000',
        cancel_url='http://localhost:8000',
    )

    return redirect(checkout_session.url, code=303)