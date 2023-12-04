from django.contrib import admin
from Shop.models import Order, BlackAndWhitePrice, ColorPrice, Sales
# Register your models here.
admin.site.register(Order)
admin.site.register(BlackAndWhitePrice)
admin.site.register(ColorPrice)
admin.site.register(Sales)
