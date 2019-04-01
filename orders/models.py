from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.name}"

class AddOns(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f"{self.name}"

class PizzaPrice(models.Model):
    sicilian = models.BooleanField(default=False)
    large = models.BooleanField(default=False)
    toppings_count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{'Large' if self.large else 'Small'} {'Sicilian ' if self.sicilian else ''}Pizza with {self.toppings_count} toppings for {self.price}"
    class Meta:
        unique_together = ('sicilian', 'large', 'toppings_count')

class Food(models.Model):
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32, choices=(('Pizza','Pizza'), ('Dinner Platter','Dinner Platter'), ('Sub','Sub'), ('Dinner','Dinner'), ('Pasta','Pasta'), ('Salad','Salad')))
    sub_type = models.CharField(max_length=32, blank=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    add_on = models.ManyToManyField(AddOns, blank=True)
    size = models.CharField(max_length=1, choices= (('S','Small'),('L','Large')),blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, blank = True)

    def __str__(self):
        toppings = ", ".join(str(top) for top in self.toppings.all())
        size = self.get_size_display()
        is_pizza = self.type == 'Pizza'
        is_sub = self.type == 'Sub'
        pizza_display = self.type if is_pizza or is_sub else ''
        tops = toppings != ''
        top_true = 'with' if tops else ''
        return f'{self.id}. {size} {self.name} {self.sub_type} {pizza_display} {top_true} {toppings}'

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    total= models.DecimalField(decimal_places=2,max_digits=99, default=0.00, blank = True)

    def __str__(self):
        return f"Order {self.id} at {self.timestamp} for {self.total}"

class OrderLine(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    food = models.ForeignKey(Food, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
