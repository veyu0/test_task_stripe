from django.contrib import admin
from django.urls import path

from stripe_app.views import get_item, buy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:id>/', get_item),
    path('buy/', buy, name='buy')
]
