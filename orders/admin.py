from django.contrib import admin
from .models import *
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Topping)
admin.site.register(PizzaPrice)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order)
admin.site.register(OrderLine)
